"""Sub module for generic helper functions."""

import csv
import datetime
import glob
import json
import os
import shutil
from decimal import Decimal
from pathlib import Path
from typing import Any, Dict, List, Union

from behave.runner import Context
from dateutil import parser  # type: ignore
from openpyxl import load_workbook


def convert_to_datetime(date_string: str) -> Union[datetime.datetime, bool]:
    """Convert to correct dataType.

    Args:
        date_string (str): The string of date to be converted to datetime.

    Returns:
        datetime: The datetime object representing the date string
    """
    if "T" in date_string:
        date_string = date_string.replace("T", " ")
    if ".0000000" in date_string:
        date_string = date_string.replace(".0000000", "")
    if "." in date_string:
        f = "%Y-%m-%d %H:%M:%S.%f"
    else:
        f = "%Y-%m-%d %H:%M:%S"
    try:
        return datetime.datetime.strptime(date_string, f)
    except ValueError as err:
        print(f"Failed to convert date_string to datetime type, Error: {err}")
        return False


def convert_to_date(date_string: str) -> Union[datetime.date, bool]:
    """Convert to date object.

    Args:
        date_string (str): Input date string

    Returns:
        [date]: Date object of date string
    """
    if "T" in date_string:
        date_string = date_string.replace("T", " ")
    if ".0000000" in date_string:
        date_string = date_string.replace(".0000000", "")
    if "." in date_string:
        f = "%Y-%m-%d %H:%M:%S.%f"
    else:
        f = "%Y-%m-%d %H:%M:%S"
    try:
        return datetime.datetime.strptime(date_string, f).date()
    except ValueError as err:
        print(f"Failed to convert date_string to datetime type, Error: {err}")
        return False


def get_date_string(context: Context) -> str:
    """Creates a data string.

    Args:
        context (Context): The context object that includes the string to be converted

    Returns:
        str: If today passed in returns today else flip date
    """
    if context.date == "today":
        batch_date = str(context.year) + "-" + str(context.month) + "-" + str(context.day)
    else:
        split_date = context.date.split("-")
        batch_date = str(split_date[2]) + "-" + str(split_date[1]) + "-" + str(split_date[0])

    return batch_date


def convert_to_decimal(number: float) -> Decimal:
    """Convert to decimal object.

    Args:
        number (float): Input Number

    Raises:
        ValueError: When unable to convert to decimal

    Returns:
        Decimal: Decimal object of passed in float
    """
    try:
        return Decimal(number).quantize(Decimal("1." + "0" * len(str(number).split(".")[1])))
    except Exception as exc:
        raise ValueError("Unable to convert " + str(number)) from exc


def is_date(string: str, fuzzy: bool = False) -> bool:
    """Return whether the string can be interpreted as a date.

    Args:
        string (str): string to check for date
        fuzzy (bool, optional): ignore unknown tokens in string if True. Defaults to False.

    Returns:
        bool: True if isDate
    """
    try:
        parser.parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def convert_string_type(string: str) -> Union[None, bool, int, datetime.datetime, str]:
    """Return whether the string can be interpreted as a date.

    Args:
        string (str): string to check for date
        fuzzy (bool, optional): ignore unknown tokens in string if True. Defaults to False.

    Returns:
        _type_: True if isDate
    """
    if string in ("None", "Null", "NULL", "null"):
        return None
    if string.isdigit():
        return int(string)
    if is_date(string):
        return convert_to_datetime(string)
    if string in ("True", "true"):
        return True
    if string in ("False", "false"):
        return False
    else:
        return string


def get_month(month: str) -> str:
    """Get month directory for uploading test data.

    Args:
        month (str): String of month to convert

    Returns:
        str: Folder to upload test data from
    """
    return f"month_{int(month)}"


def get_all_files_in_a_directory(directory_path: str, directory: bool = False) -> list:
    """Returns list of files in a directory.

    Args:
        directory_path (str): Path to directory
        directory (bool): return directory not files if True (defaults to False)

    Returns:
        list: List of file paths
    """
    if directory:
        return [f for f in glob.glob(f"{directory_path}/*", recursive=True) if os.path.isdir(f)]
    else:
        return [f for f in glob.glob(f"{directory_path}/*", recursive=True) if os.path.isfile(f)]


def get_base_name(file: str) -> str:
    """Returns file basename from file path.

    Args:
        file (str): File path

    Returns:
        [str]:File basename
    """
    return os.path.basename(file)


def load_json(path: str) -> Dict[str, object]:
    """Reads a json file and returns a json object.

    Args:
        path (str): File path

    Returns:
        [JSON]:Json object
    """
    with open(path, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def convert_path(path: str) -> Path:
    """Pass in a string of a path e.g 'test/path' and will return a Path object that will work for any os.

    Args: path (str): String of the path to load

    Returns:
        Path: New Path object
    """
    return Path(path)


def write_log_data(log_file_name: str, log_data: str) -> None:
    """Write data to a file, useful for debugging CICD.

    Args:
        log_file_name (str): Name of the log file to create
        log_data (str): String to write to the logfile
    """
    with open(log_file_name, "a", encoding="utf-8") as f:
        f.write(str(log_data) + "\n")
        f.close()


def parse_datetime(value: Any) -> Any:
    """Parse a datetime string and update it to a datetime object.

    Args:
        value (Any): Anything to parse through

    Returns:
        Any: Original object with parsed datetime
    """
    if isinstance(value, dict):
        for k, v in value.items():
            value[k] = parse_datetime(v)
    elif isinstance(value, list):
        for index, row in enumerate(value):
            value[index] = parse_datetime(row)
    elif isinstance(value, str) and value:
        try:
            value = parser.parse(value)
        except (ValueError, AttributeError):
            return value  # Early return in case of parsing error
        if isinstance(value, datetime.datetime) and value.date() == datetime.datetime.today().date():
            return value.time()  # Early return if the date is today
    return value


def load_json_and_parse(path: str) -> Dict[str, Any]:
    """Reads a JSON file and returns a JSON object with parsed dates.

    Args:
        path (str): File path

    Returns:
        json: JSON object
    """
    with open(path, encoding="utf-8") as json_file:
        data = json.load(json_file, object_hook=parse_datetime)
    return data


def remove_from_dir_or_file(folder: str) -> str:
    """Remove data in data folder downloaded from the containers.

    Args:
        folder (_type_): _description_

    Raises:
        ex: RuntimeError, TypeError, AttributeError, FileNotFoundError, NotADirectoryError

    Returns:
        str: "Folder does not exist" if the passed in folder is not found.
    """
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except (
                RuntimeError,
                TypeError,
                AttributeError,
                FileNotFoundError,
                NotADirectoryError,
            ) as ex:
                print(f"Failed to delete {file_path}, Reason: {ex}")
                raise ex
        return "Deletions are complete."
    else:
        raise FileNotFoundError("Folder does not exist")


def delete_local_file(file_path: str) -> str:
    """Check if file exists before deleting file.

    Args:
        file_path (str): path to file

    Raises:
        ex: RuntimeError, TypeError, AttributeError, FileNotFoundError, NotADirectoryError

    Returns:
        str: "The files does not exist" if the file does not exist.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("The file does not exist")
            return "The file does not exist"
    except (
        RuntimeError,
        TypeError,
        AttributeError,
        FileNotFoundError,
        NotADirectoryError,
    ) as ex:
        print(f"Failed to delete file, from path - {file_path}, Error: {ex}")
        raise ex
    return "Deletions successful"


def remove_from_dir_or_file_if_exists(folder: str) -> str:
    """Remove data in data folder downloaded from the containers.

    Args:
        folder (_str_): path to the folder

    Returns:
        str: "Folder does not exist" if the passed in folder is not found.
    """
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except (
                RuntimeError,
                TypeError,
                AttributeError,
                FileNotFoundError,
                NotADirectoryError,
            ) as ex:
                print(f"Failed to delete {file_path}, Reason: {ex}")
                raise ex
        return "Deletions are complete."
    else:
        return "Folder does not exist"


def create_folder_if_not_exists(folder_path: str) -> None:
    """Creates a folder if it does not exist.

    Args:
        folder_path (str): Path to the folder to create.
    """
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def load_main_data_catalogue(path: str = "") -> str:
    """Loads the latest data catalogue from the ../DATAMODELS/DATACATALOGUE/ directory.

    Args:
        path (str, optional): Path to the data catalogue to load. Leave as "" for default.

    Returns:
        str: Path and name of the current data catalogue to load.
    """
    if path == "":
        location = "../DATAMODELS/DATACATALOGUE/*.xlsx"
    else:
        location = f"{path}/*.xlsx"
    file_list = []
    for file in glob.glob(location):
        file_list.append(file)
    return file_list[0]


def load_csv_to_list_of_dicts(csv_file_path: str) -> List[Dict[str, object]]:
    """Load a CSV file and return a list of dictionaries.

    Args:
        csv_file_path (str): Location of the CSV file to load.

    Returns:
        List[Dict[str, object]]: Returns a list of dictionaries from the CSV file.
    """
    # List to hold dictionaries
    list_of_dicts = []

    # Open the CSV file and read data into a list of dictionaries
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_of_dicts.append(row)

    return list_of_dicts
