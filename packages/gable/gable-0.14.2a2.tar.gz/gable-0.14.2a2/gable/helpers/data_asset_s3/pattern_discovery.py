import os
import re
from datetime import datetime
from enum import Enum
from typing import Optional
from urllib.parse import quote, unquote

from botocore.exceptions import ClientError
from gable.helpers.data_asset_s3.logger import log_debug, log_error, log_trace
from gable.helpers.data_asset_s3.path_pattern_manager import (
    DAY_REGEX,
    HOUR_REGEX,
    MINUTE_REGEX,
    MONTH_REGEX,
    YEAR_REGEX,
    PathPatternManager,
)
from gable.helpers.logging import log_execution_time
from mypy_boto3_s3 import S3Client
from mypy_boto3_s3.type_defs import ObjectTypeDef


class SUPPORTED_FILE_TYPES(Enum):
    CSV = ".csv"
    JSON = ".json"
    PARQUET = ".parquet"
    ORC = ".orc"
    ORC_SNAPPY = ".orc.sz"


SUPPORTED_FILE_TYPES_SET = set({file_type.value for file_type in SUPPORTED_FILE_TYPES})

DATE_PART_DELIMITERS = "[-_:]{0,2}"
FULL_DATE_MINUTE_REGEX = f"({YEAR_REGEX}){DATE_PART_DELIMITERS}({MONTH_REGEX}){DATE_PART_DELIMITERS}({DAY_REGEX}){DATE_PART_DELIMITERS}({HOUR_REGEX}){DATE_PART_DELIMITERS}({MINUTE_REGEX})"
FULL_DATE_HOUR_REGEX = f"({YEAR_REGEX}){DATE_PART_DELIMITERS}({MONTH_REGEX}){DATE_PART_DELIMITERS}({DAY_REGEX}){DATE_PART_DELIMITERS}({HOUR_REGEX})"
FULL_DATE_DAY_REGEX = f"({YEAR_REGEX}){DATE_PART_DELIMITERS}({MONTH_REGEX}){DATE_PART_DELIMITERS}({DAY_REGEX})"
FULL_DATE_REGEXES = [
    FULL_DATE_MINUTE_REGEX,
    FULL_DATE_HOUR_REGEX,
    FULL_DATE_DAY_REGEX,
]


class DATETIME_DIRECTORY_TYPE(Enum):
    YEAR = YEAR_REGEX
    MONTH = MONTH_REGEX
    DAY = DAY_REGEX
    HOUR = HOUR_REGEX
    MINUTE = MINUTE_REGEX
    FULL_MINUTE = FULL_DATE_MINUTE_REGEX
    FULL_HOUR = FULL_DATE_HOUR_REGEX
    FULL_DAY = FULL_DATE_DAY_REGEX


@log_execution_time
def discover_patterns_from_s3_bucket(
    client: S3Client,
    bucket_name: str,
    include: list[str],
    start_date: datetime,
    end_date: Optional[datetime] = None,
    files_per_directory: int = 1000,
    ignore_timeframe_bounds: bool = False,
) -> dict[str, dict[str, Optional[datetime]]]:
    """
    Discover patterns in an S3 bucket.

    Args:
        client: S3 client.
        bucket_name (str): S3 bucket.
        start_date (datetime): The furthest back in time we'll crawl to discover patterns
        end_date (datetime, optional): The most recent point in time we'll crawl to discover patterns. Defaults to None, which implies crawl to now.
        include (list[str], optional): list of prefixes to include
        files_per_directory (int, optional): Number of files per directory. Defaults to 1000.

    Returns:
        list[str]: List of patterns.
    """
    log_trace("Starting pattern discovery in bucket: {}", bucket_name)
    _validate_bucket_exists(client, bucket_name)
    path_manager = PathPatternManager()
    _discover_file_paths_from_s3_bucket(
        client,
        path_manager,
        bucket_name,
        "",
        include,
        files_per_directory,
        ignore_timeframe_bounds,
        start_date,
        end_date,
    )
    return path_manager.get_pattern_to_actual_paths()


def _discover_file_paths_from_s3_bucket(
    client: S3Client,
    path_manager: PathPatternManager,
    bucket_name: str,
    prefix: str,
    include: list[str],
    max_ls_results,
    ignore_timeframe_bounds: bool,
    start_date: datetime,
    end_date: Optional[datetime] = None,
    year: Optional[int] = None,
    month: Optional[int] = None,
    day: Optional[int] = None,
    hour: Optional[int] = None,
    minute: Optional[int] = None,
):
    """
    Discover patterns in an S3 bucket via populating pattern_manager recursively.

    Args:
        client: S3 client.
        path_manager (PathPatternManager): Path pattern manager whose underlying structures are populated by this function
        bucket_name (str): S3 bucket.
        prefix (str): Prefix.
        start_date (datetime): The furthest back in time we'll crawl to discover patterns
        end_date (datetime, optional): The most recent point in time we'll crawl to discover patterns. Defaults to None indicating "now".
        year (int, optional): The year if we're in a year directory. Defaults to None.
        month (int, optional): The month if we're in a month directory. Defaults to None.
        day (int, optional): The day if we're in a day directory. Defaults to None.
        hour (int, optional):  The hour if we're in an hour directory. Defaults to None.
        minute (int, optional): The minute if we're in a minute directory. Defaults to None.
        max_ls_results (int, optional): Maximum number of results to return when listing items in a prefix. Defaults to 1000.
    """
    if (
        include
        and len(include) > 0
        and not any([incl in prefix or prefix in incl for incl in include])
    ):
        return
    try:
        files = [
            obj["Key"] for obj in _list_files(client, bucket_name, max_ls_results, prefix)  # type: ignore
        ]

        # If we're in a day, hour, or minute folder, check for files and add them regardless of the name
        if files and any([day, hour, minute]):
            new_patterns = path_manager.add_filepaths(files)
            if new_patterns:
                log_trace(f"({prefix})\tDiscovered {new_patterns} new pattern(s)")
            else:
                log_trace(f"({prefix})\tNo new pattern(s)")
        elif files:
            # Otherwise, list files and check to see if they have a datetime in them. This catches files like
            # data/shipments_2024-01-01.csv
            datetime_files = [
                f
                for f in files
                if any(map(lambda x: re.search(x, f) is not None, FULL_DATE_REGEXES))
            ]
            # For each file, extract the year, month, day, hour, minute and verify it falls within the start
            # and end date
            datetime_files_to_add = []
            for f in datetime_files:
                success, _year, _month, _day, _hour, _minute = (
                    _get_ymdhm_from_datetime_filename(os.path.basename(f))
                )
                if success and (
                    ignore_timeframe_bounds
                    or _is_within_look_back_window(
                        start_date, end_date, _year, _month, _day, _hour, _minute
                    )
                ):
                    datetime_files_to_add.append(f)
            new_patterns = path_manager.add_filepaths(datetime_files_to_add)
            if new_patterns:
                log_trace(f"({prefix})\tDiscovered {new_patterns} new pattern(s)")
            else:
                log_trace(f"({prefix})\tNo new pattern(s)")

        directories = _list_directories(client, bucket_name, prefix, max_ls_results)
        grouped_datetime_directories = _group_datetime_directories_by_type(
            directories, year, month, day, hour, minute
        )
        # Split out the non-datetime directories from the datetime directories
        non_datetime_directories = grouped_datetime_directories.pop(None, [])
        # Recursively traverse all of the non-datetime directories, but first, another safety check...
        if len(non_datetime_directories) > 0 and _check_for_alpha_difference(
            non_datetime_directories
        ):
            for dir in non_datetime_directories:
                _discover_file_paths_from_s3_bucket(
                    client,
                    path_manager,
                    bucket_name,
                    os.path.join(prefix, dir) + "/",
                    ignore_timeframe_bounds=ignore_timeframe_bounds,
                    start_date=start_date,
                    end_date=end_date,
                    year=year,
                    month=month,
                    day=day,
                    hour=hour,
                    minute=minute,
                    max_ls_results=max_ls_results,
                    include=include,
                )

        elif len(non_datetime_directories) > 0:
            log_debug(
                f"Found non-datetime directories with no alphabetical difference in {bucket_name}/{prefix}, (example {non_datetime_directories[0]}) skipping further traversal",
            )
        # Now handle the datetime directories
        for (
            datetime_directory_type,
            datetime_directories,
        ) in grouped_datetime_directories.items():
            if datetime_directory_type is not None and len(datetime_directories) > 0:
                # Sort the directories in reverse order so we can break out when we hit the first
                # datetime outside of the start_date
                datetime_directories.sort(reverse=True)
                for datetime_directory in datetime_directories:
                    success, _year, _month, _day, _hour, _minute = (
                        _get_ymdhm_from_datetime_directory(
                            datetime_directory_type,
                            datetime_directory,
                            year,
                            month,
                            day,
                            hour,
                            minute,
                        )
                    )
                    if success and (
                        ignore_timeframe_bounds
                        or _is_within_look_back_window(
                            start_date, end_date, _year, _month, _day, _hour, _minute
                        )
                    ):
                        _discover_file_paths_from_s3_bucket(
                            client,
                            path_manager,
                            bucket_name,
                            os.path.join(prefix, datetime_directory) + "/",
                            ignore_timeframe_bounds=ignore_timeframe_bounds,
                            start_date=start_date,
                            end_date=end_date,
                            year=_year,
                            month=_month,
                            day=_day,
                            hour=_hour,
                            minute=_minute,
                            max_ls_results=max_ls_results,
                            include=include,
                        )
                    elif not success:
                        log_debug(
                            f"Failed to parse datetime directory {datetime_directory} in {bucket_name}/{prefix}, skipping further traversal",
                        )
    except Exception as e:
        log_error("Failed during pattern discovery in {}: {}", bucket_name, str(e))
        raise


def _is_within_look_back_window(
    start_date: datetime,
    end_date: Optional[datetime],
    year: Optional[int],
    month: Optional[int],
    day: Optional[int],
    hour: Optional[int],
    minute: Optional[int],
) -> bool:
    # If we're looking at a year directory, we only need to check the year
    if year is not None and not any([month, day, hour, minute]):
        return year >= start_date.year
    # If we're looking at a month directory, trim the start and end dates to the month
    # for the comparison
    if year is not None and month is not None and not any([day, hour, minute]):
        start_date_month = datetime(start_date.year, start_date.month, 1)
        end_date_month = (
            datetime(end_date.year, end_date.month, 1) if end_date else None
        )
        return datetime(year, month, 1) >= start_date_month and (
            end_date_month is None or datetime(year, month, 1) <= end_date_month
        )
    # Otherwise we have at least year, month, day - hour and minute are filled
    # in with 0 if not present
    if year and month and day:
        f_dt = datetime(year, month, day, hour or 0, minute or 0, 0)
        if f_dt >= start_date and (end_date is None or f_dt <= end_date):
            return True
    return False


def _get_ymdhm_from_datetime_directory(
    datetime_directory_type: DATETIME_DIRECTORY_TYPE,
    directory: str,
    year: Optional[int] = None,
    month: Optional[int] = None,
    day: Optional[int] = None,
    hour: Optional[int] = None,
    min: Optional[int] = None,
) -> tuple[
    bool, Optional[int], Optional[int], Optional[int], Optional[int], Optional[int]
]:
    directory = super_unquote(directory).rstrip("/")
    if datetime_directory_type == DATETIME_DIRECTORY_TYPE.YEAR:
        return True, int(directory), None, None, None, None
    if datetime_directory_type == DATETIME_DIRECTORY_TYPE.MONTH:
        return True, year, int(directory), None, None, None
    if datetime_directory_type == DATETIME_DIRECTORY_TYPE.DAY:
        return True, year, month, int(directory), None, None
    if datetime_directory_type == DATETIME_DIRECTORY_TYPE.HOUR:
        return True, year, month, day, int(directory), None
    if datetime_directory_type == DATETIME_DIRECTORY_TYPE.MINUTE:
        return True, year, month, day, hour, int(directory)
    if datetime_directory_type == DATETIME_DIRECTORY_TYPE.FULL_MINUTE:
        matches = re.match(FULL_DATE_MINUTE_REGEX, directory)
        if matches is None:
            return False, None, None, None, None, None
        return (
            True,
            int(matches.group(1)),
            int(matches.group(2)),
            int(matches.group(3)),
            int(matches.group(4)),
            int(matches.group(5)),
        )
    if datetime_directory_type == DATETIME_DIRECTORY_TYPE.FULL_HOUR:
        matches = re.match(FULL_DATE_HOUR_REGEX, directory)
        if matches is None:
            return False, None, None, None, None, None
        return (
            True,
            int(matches.group(1)),
            int(matches.group(2)),
            int(matches.group(3)),
            int(matches.group(4)),
            None,
        )
    if datetime_directory_type == DATETIME_DIRECTORY_TYPE.FULL_DAY:
        matches = re.match(FULL_DATE_DAY_REGEX, directory)
        if matches is None:
            return False, None, None, None, None, None
        return (
            True,
            int(matches.group(1)),
            int(matches.group(2)),
            int(matches.group(3)),
            None,
            None,
        )
    return False, None, None, None, None, None


def _get_ymdhm_from_datetime_filename(
    directory: str,
) -> tuple[
    bool, Optional[int], Optional[int], Optional[int], Optional[int], Optional[int]
]:
    directory = super_unquote(directory).rstrip("/")
    search_results = re.search(FULL_DATE_MINUTE_REGEX, directory)
    if search_results:
        return (
            True,
            int(search_results.group(1)),
            int(search_results.group(2)),
            int(search_results.group(3)),
            int(search_results.group(4)),
            int(search_results.group(5)),
        )
    search_results = re.search(FULL_DATE_HOUR_REGEX, directory)
    if search_results:
        return (
            True,
            int(search_results.group(1)),
            int(search_results.group(2)),
            int(search_results.group(3)),
            int(search_results.group(4)),
            None,
        )
    search_results = re.search(FULL_DATE_DAY_REGEX, directory)
    if search_results:
        return (
            True,
            int(search_results.group(1)),
            int(search_results.group(2)),
            int(search_results.group(3)),
            None,
            None,
        )
    return False, None, None, None, None, None


def _check_for_alpha_difference(directories: list[str]) -> bool:
    """
    Checks to see if there is a difference in the list of directory names if all numbers are removed. This is used
    to detect a folder pattern we don't understand, but that has a consistent pattern. We don't want to traverse these
    directories, or we may end up iterating over a large number of directories and consider them all separate data assets.

    Example: ["0000001", "0000002", "0000003"] would return False, because the only difference is the numbers

    Args:
        directories (list[str]): List of directories.

    Returns:
        bool: True if there is a difference in alphabetical order, False otherwise.
    """
    # Edge case: if there's only one directory just return True
    if len(directories) == 1:
        return True
    stripped_directories = [re.sub(r"\d", "", directory) for directory in directories]
    return len(set(stripped_directories)) > 1


def _group_datetime_directories_by_type(
    directories: list[str], year=None, month=None, day=None, hour=None, minute=None
) -> dict[Optional[DATETIME_DIRECTORY_TYPE], list[str]]:
    directory_groups = {}
    for directory in directories:
        directory_type = _get_datetime_directory_type(
            directory, year, month, day, hour, minute
        )

        if directory_type not in directory_groups:
            directory_groups[directory_type] = []
        directory_groups[directory_type].append(directory)
    return directory_groups


def _get_datetime_directory_type(
    directory: str, year=None, month=None, day=None, hour=None, minute=None
) -> Optional[DATETIME_DIRECTORY_TYPE]:
    # Trim the directory to remove any trailing slashes
    directory = super_unquote(directory).rstrip("/")
    # If we're already in a minute directory, don't go any deeper
    if minute is not None:
        return None
    # Otherwise check if the directory matches the next logical datetime part regex
    if (
        hour is not None
        and re.fullmatch(DATETIME_DIRECTORY_TYPE.MINUTE.value, directory) is not None
    ):
        return DATETIME_DIRECTORY_TYPE.MINUTE
    if (
        day is not None
        and re.fullmatch(DATETIME_DIRECTORY_TYPE.HOUR.value, directory) is not None
    ):
        return DATETIME_DIRECTORY_TYPE.HOUR
    if (
        month is not None
        and re.fullmatch(DATETIME_DIRECTORY_TYPE.DAY.value, directory) is not None
    ):
        return DATETIME_DIRECTORY_TYPE.DAY
    if (
        year is not None
        and re.fullmatch(DATETIME_DIRECTORY_TYPE.MONTH.value, directory) is not None
    ):
        return DATETIME_DIRECTORY_TYPE.MONTH
    # At this point we're not in any sort of datetime directory, so check if it's a year directory, or a full date directory
    if re.fullmatch(DATETIME_DIRECTORY_TYPE.YEAR.value, directory) is not None:
        return DATETIME_DIRECTORY_TYPE.YEAR
    if re.match(FULL_DATE_MINUTE_REGEX, directory) is not None:
        return DATETIME_DIRECTORY_TYPE.FULL_MINUTE
    if re.match(FULL_DATE_HOUR_REGEX, directory) is not None:
        return DATETIME_DIRECTORY_TYPE.FULL_HOUR
    if re.match(FULL_DATE_DAY_REGEX, directory) is not None:
        return DATETIME_DIRECTORY_TYPE.FULL_DAY
    return None


def _list_directories(
    client: S3Client, bucket_name: str, prefix: str, max_ls_results: int = 1000
) -> list[str]:
    """
    List all directories in an S3 bucket. Returns only the directory names, not the full path.

    Args:
        client: S3 client.
        bucket_name (str): S3 bucket.
        prefix (str): Prefix. This is used for recursive calls and differs from kwargs["include"] which is a configuration option.
        max_ls_results (int, optional): Maximum number of results to return when listing items in a prefix. Defaults to 1000.
    Returns:
        list[str]: List of directories.
    """
    paginator = client.get_paginator("list_objects_v2")

    pagination_result = (
        paginator.paginate(
            Bucket=bucket_name,
            Prefix=prefix,
            Delimiter="/",
            PaginationConfig={"MaxItems": max_ls_results},
        ).search("CommonPrefixes")
        or []
    )

    filtered_results = []
    for result in pagination_result:
        if result is not None and "Prefix" in result:
            filtered_results.append(result["Prefix"])

    return [item.rstrip("/").split("/")[-1] for item in filtered_results]


def _list_files(
    client: S3Client, bucket_name: str, max_files: int, prefix: str = ""
) -> list[ObjectTypeDef]:
    """
    List objects in an S3 bucket.

    Args:
        client: S3 client.
        bucket_name (str): S3 bucket.
        max_files (int): Maximum number of files to list.
        prefix (str, optional): Prefix. Defaults to None.

    Returns:
        dict[str, object]: mapping of file names to contents.
    """
    log_trace(
        "Starting to paginate files in bucket: {} with prefix: {}", bucket_name, prefix
    )
    paginator = client.get_paginator("list_objects_v2")
    files: list[ObjectTypeDef] = []
    for page in paginator.paginate(
        Bucket=bucket_name,
        Prefix=prefix,
        PaginationConfig={"MaxItems": max_files},
    ):
        for obj in page.get("Contents", []):
            files.append(obj)
    log_trace("Completed listing files, total files gathered: {}", len(files))
    return files


def is_supported_file_type(file_path: str) -> bool:
    """
    Check if the file type is supported.

    Args:
        file_path (str): File path.

    Returns:
        bool: True if the file type is supported, False otherwise.
    """
    return any(
        [file_path.endswith(file_type) for file_type in SUPPORTED_FILE_TYPES_SET]
    )


def super_unquote(s: str):
    new_s, _ = super_unquote_n(s)
    return new_s


def super_unquote_n(s: str):
    if s == unquote(s):
        return s, 0
    old_s = s
    s = unquote(s)
    quote_count = 1
    while s != old_s:
        old_s = s
        s = unquote(s)
        quote_count += 1
    return s, quote_count


def super_quote(s: str, count):
    for _ in range(count):
        s = quote(s)
    return s


def _validate_bucket_exists(client, bucket_name: str) -> None:
    log_trace("Validating existence of bucket: {}", bucket_name)
    try:
        client.head_bucket(Bucket=bucket_name)
        log_trace("Bucket exists: {}", bucket_name)
    except client.exceptions.ClientError as e:
        if isinstance(e, ClientError):
            error_code = int(e.response["Error"]["Code"])  # type: ignore
            if error_code == 404:
                print(f"Bucket {bucket_name} does not exist.")
                log_error("Bucket does not exist for {}: {}", bucket_name, str(e))
            elif error_code == 403:
                print(f"Access to bucket {bucket_name} is forbidden.")
                log_error(
                    "Access to bucket is forbidden for {}: {}", bucket_name, str(e)
                )
        raise ValueError(
            f"Bucket {bucket_name} does not exist or is not accessible. Check that AWS credentials are set up correctly."
        )


def flatten(lists: list[list]):
    return list((item for sublist in lists for item in sublist))


def replace_date_placeholders(pattern: str, date_str: str = "") -> str:
    """
    Replace date placeholders in the pattern with the provided date string or today's date if not provided.

    Args:
        pattern (str): The pattern containing placeholders.
        date_str (str, optional): Date in 'YYYY-MM-DD' format to inject into the pattern. Defaults to today's date.

    Returns:
        str: The pattern with date placeholders replaced.
    """
    # Use the current date if no date string is provided
    if date_str == "":
        date = datetime.now()
    else:
        date = datetime.strptime(date_str, "%Y-%m-%d")

    date = datetime.strptime(date_str, "%Y-%m-%d")
    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")

    # Replace the placeholders within the curly braces
    pattern = (
        pattern.replace("{YYYY}", year).replace("{MM}", month).replace("{DD}", day)
    )
    pattern = pattern.replace("{YYYY-MM-DD}", f"{year}-{month}-{day}")

    # Replace placeholders without curly braces if directly included in the string
    pattern = pattern.replace("{YYYYMMDD}", f"{year}{month}{day}")
    pattern = pattern.replace("YYYY", year).replace("MM", month).replace("DD", day)

    return pattern
