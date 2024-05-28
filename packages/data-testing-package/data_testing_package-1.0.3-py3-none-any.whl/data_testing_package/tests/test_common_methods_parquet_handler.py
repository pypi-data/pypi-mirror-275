"""Unit tests for data_testing_package.common_method.parquet_handler."""
from pathlib import Path
from pandas import DataFrame
from src.data_testing_package.common_methods import parquet_handler
import Global


def test_get_expected_results_parquetfile() -> None:
    """Test get_expected_results_parquetfile."""
    assert isinstance(parquet_handler.get_expected_results_parquetfile(Global.sample_parquet_file), DataFrame) is True, "get_expected_results_parquetfile should return a DataFrame"


def test_check_dataframes_are_equal(file1=Global.sample_csv, file2=Global.sample_csv) -> None:
    """Test check_dataframes_are_equal."""
    data_frame_1 = parquet_handler.read_file_into_dataframe(file1)
    data_frame_2 = parquet_handler.read_file_into_dataframe(file2)
    assert parquet_handler.check_dataframes_are_equal(data_frame_1, data_frame_2) is True, "DataFrames should be equal"


def test_dataframe_comparison(file1=Global.sample_csv, file2=Global.sample2_csv) -> None:
    """Test if the function raises an exception when dataframes are not equal"""
    data_frame_1 = parquet_handler.read_file_into_dataframe(file1)
    data_frame_2 = parquet_handler.read_file_into_dataframe(file1)
    data_frame_3 = parquet_handler.read_file_into_dataframe(file2)
    assert parquet_handler.dataframe_comparison(data_frame_1, data_frame_2) == "DataFrames are the same", "DataFrames should be equal"  # type: ignore
    try:
        parquet_handler.dataframe_comparison(data_frame_1, data_frame_3)
    except AssertionError as ex:
        assert type(ex).__name__ == "AssertionError", "AssertionError should be raised when DataFrames are not equal."


def test_remove_files_from_repo(txt_file=Global.sample_txt) -> None:
    """Test remove_files_from_repo."""
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("sample file to be removed.")
    assert parquet_handler.remove_files_from_repo(txt_file) is True, "remove_files_from_repo failed to remove files."


def test_read_file_into_dataframe(csv_file=Global.sample_csv) -> None:
    """Test read_file_into_dataframe."""
    assert isinstance(parquet_handler.read_file_into_dataframe(csv_file), DataFrame), "read_file_into_dataframe failed to convert to dataframe."


def test_validate_columns(file1 = Global.No_Missing_column) -> None:
    """ Test validate_missing_column function when file has no missing column """
    assert parquet_handler.validate_columns(file1) is True, "Some columns are missing"


def test_validate_missing_column(file1 = Global.Missing_column) -> None:
    """ Test validate_missing_column function when file has missing column """
    assert parquet_handler.validate_columns(file1) is False, "No columns are missing"


def  test_remove_columns_from_df() -> None:
    "Test remove_columns_from_df"
    assert parquet_handler.remove_columns_from_df(Global.No_Missing_column, ["date", "time"]) is True, "Dataframe columns are not dropped"


# def test_remove_dir_and_files_within_it(tmp_path: Path) -> None:
#     """Test to remove files or directories within a directory.

#     Args:
#         tmp_path (Path): Temp path for testing.
#     """
#     # Create a temporary directory with files for testing
#     test_dir = tmp_path / "test_dir"
#     test_file = test_dir / "test_file.txt"
#     test_dir.mkdir(parents=True)
#     test_file.write_text("test content")

#     # Test the function to remove the temporary directory and files
#     remove_dir_and_files_within_it(test_dir)
#     assert not test_dir.exists()

#     # Test when the directory doesn't exist
#     non_existing_dir = tmp_path / "non_existing_dir"
#     result = remove_dir_and_files_within_it(non_existing_dir)
#     assert result is None

