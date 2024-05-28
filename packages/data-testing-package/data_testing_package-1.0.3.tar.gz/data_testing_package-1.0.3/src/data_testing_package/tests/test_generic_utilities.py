"""Unit tests for the Data Testing Package."""

import datetime
import os
from decimal import Decimal
from pathlib import Path

from behave.runner import Context
from data_testing_package.common_methods import utilities


def test_convert_to_datetime() -> None:
    """Test for convert_to_datetime."""
    assert isinstance(utilities.convert_to_datetime("2040-01-01 10:00:00"), datetime.date) is True, "Not datetime object"


def test_convert_to_date() -> None:
    """Test for convert_to_date."""
    assert isinstance(utilities.convert_to_date("2040-01-01 10:00:00"), datetime.date) is True, "Not datetime object"
    assert isinstance(utilities.convert_to_date("2040-01-01T10:00:00"), datetime.date) is True, "Not datetime object"
    assert isinstance(utilities.convert_to_date("2040-01-01 10:00:00.0000000"), datetime.date) is True, "Not datetime object"
    assert utilities.convert_to_date("test") is False, "String did not return False"


def test_get_date_string() -> None:
    """Test for get_date_string."""
    context = Context
    context.date = "today"
    context.year = "2020"
    context.month = "12"
    context.day = "25"
    assert utilities.get_date_string(context) == "2020-12-25", "Date string didn't convert"
    context.date = "2020-12-25"
    assert utilities.get_date_string(context) == "25-12-2020", "Date string didn't convert"


def test_convert_to_decimal() -> None:
    """Test conversion to decimal."""
    assert isinstance(utilities.convert_to_decimal(340945.95), Decimal), "Not Decimal object"
    assert isinstance(utilities.convert_to_decimal(5555.01), Decimal), "Not Decimal object"
    assert isinstance(utilities.convert_to_decimal(345.95), Decimal), "Not Decimal object"


def test_is_date() -> None:
    """Test is_date."""
    assert utilities.is_date("TEST") is False, "is_date object expected_data is not correct"
    assert utilities.is_date("2020-12-25") is True, "is_date object expected_data is not correct"
    assert utilities.is_date("25-12-2020") is True, "is_date object expected_data is not correct"
    assert utilities.is_date("2040-01-01 10:00:00") is True, "is_date object expected_data is not correct"
    assert utilities.is_date("2040-01-01T10:00:00") is True, "is_date object expected_data is not correct"
    assert utilities.is_date("2040-01-01 10:00:00.0000000") is True, "is_date object expected_data is not correct"


def test_convert_string_type() -> None:
    """Test for convert_string_type."""
    assert utilities.convert_string_type("1") == 1, "String didn't convert to int"
    assert utilities.convert_string_type("None") is None, "String didn't convert to None"
    assert utilities.convert_string_type("null") is None, "String didn't convert to None"
    assert utilities.convert_string_type("True") is True, "String didn't convert to bool"
    assert utilities.convert_string_type("False") is False, "String didn't convert to bool"


def test_get_month() -> None:
    """Test get_month."""
    assert utilities.get_month("01") == "month_1", "get_month should return month_X"
    assert utilities.get_month("02") == "month_2", "get_month should return month_X"
    assert utilities.get_month("03") == "month_3", "get_month should return month_X"
    assert utilities.get_month("04") == "month_4", "get_month should return month_X"
    assert utilities.get_month("12") == "month_12", "get_month should return month_X"


def test_get_all_files_in_a_directory() -> None:
    """Test get_all_files_in_a_directory and raises an exception if file doesnt exit in a directory."""
    assert utilities.get_all_files_in_a_directory(".\\tests\\folder_for_file_check", False) == [
        ".\\tests\\folder_for_file_check\\sample.file"
    ], "get_all_files_in_directory should return list of files"
    assert ".\\tests\\folder_for_get_all_files_in_a_directory_test" in utilities.get_all_files_in_a_directory(
        ".\\tests\\", True
    ), "get_all_files_in_directory with True  should return list of folders"


def test_get_base_name() -> None:
    """Test get_base_name."""
    assert utilities.get_base_name(".\\tests\\test_generic_utilities.py") == "test_generic_utilities.py", "get_base_name should return basename"


def test_load_json() -> None:
    """Test load_json."""
    assert utilities.load_json(".\\tests\\test.json") == {"String": "TEST"}, "JSON should be loaded correctly"


def test_convert_path() -> None:
    """Test convert_path."""
    assert isinstance(utilities.convert_path(".\\tests\\"), Path) is True, "Path should be converted correctly to Path object"


def test_write_log_data() -> None:
    """Test write_log_data."""
    utilities.write_log_data(".\\tests\\test_log_file.log", "written test data")
    file = Path(".\\tests\\test_log_file.log")
    assert file.is_file() is True, "File has not been created"
    with open(".\\tests\\test_log_file.log", encoding="utf-8") as log_file:
        text = log_file.readlines()
        assert "written test data" in text[0], "Data written to file is not correct"
    os.remove(".\\tests\\test_log_file.log")


def test_load_json_and_parse() -> None:
    """Test load_json_and_parse."""
    assert utilities.load_json_and_parse(".\\tests\\test.json") == {"String": "TEST"}, "JSON should be loaded correctly"


def test_remove_from_dir_or_file() -> None:
    """Test remove_from_dir_or_file."""
    with open(".\\tests\\folder_for_get_all_files_in_a_directory_test\\sample_file.txt", mode="x", encoding="utf-8") as sample_file:
        sample_file.write("This is a sample file")

    utilities.remove_from_dir_or_file(".\\tests\\folder_for_get_all_files_in_a_directory_test\\")
    assert utilities.get_all_files_in_a_directory(".\\tests\\folder_for_get_all_files_in_a_directory_test\\", False) != [
        ".\\tests\\folder_for_get_all_files_in_a_directory_test\\sample_file.txt"
    ], "sample_file.txt should have been removed"

    try:
        utilities.remove_from_dir_or_file(".\\tests\\folder_\\")
    except FileNotFoundError as ex:
        assert type(ex).__name__ == "FileNotFoundError", "AssertionError should be raised when DataFrames are not equal."
        assert str(ex) == "Folder does not exist", "AssertionError should be raised when DataFrames are not equal."


def test_delete_local_file() -> None:
    """Test delete_local_file."""
    with open(".\\tests\\folder_for_get_all_files_in_a_directory_test\\sample_file.txt", mode="x", encoding="utf-8") as sample_file:
        sample_file.write("This is a sample file")
    utilities.delete_local_file(".\\tests\\folder_for_get_all_files_in_a_directory_test\\sample_file.txt")
    assert utilities.get_all_files_in_a_directory(".\\tests\\folder_for_get_all_files_in_a_directory_test\\", False) != [
        ".\\tests\\folder_for_get_all_files_in_a_directory_test\\sample_file.txt"
    ], "sample_file.txt should have been removed"
    assert (
        utilities.delete_local_file(".\\tests\\folder_for_get_all_files_in_a_directory_test\\sample_file.txt") == "The file does not exist"
    ), 'Should return "The file does not exist" if file does not exist'


def test_remove_from_dir_or_file_if_exists() -> None:
    """Test when the folder does not exist."""
    folder = "non_existent_folder"
    result = utilities.remove_from_dir_or_file_if_exists(folder)
    assert result == "Folder does not exist"


def test_create_folder_if_not_exists(tmpdir: Path) -> None:
    """Test for create_folder_if_not_exists.

    Args:
        tmpdir (Path): Location where folder should be created.
    """
    # Create a temporary directory for testing
    folder_path = os.path.join(tmpdir, "test_folder")

    # Test creating a folder that does not exist
    utilities.create_folder_if_not_exists(folder_path)
    assert os.path.exists(folder_path)

    # Test creating a folder that already exists
    utilities.create_folder_if_not_exists(folder_path)
    assert os.path.exists(folder_path)
