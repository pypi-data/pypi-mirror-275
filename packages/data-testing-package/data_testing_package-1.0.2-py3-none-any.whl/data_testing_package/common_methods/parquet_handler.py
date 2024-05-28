"""Parquet file handling and comparing functions."""
import os
import json
from pathlib import Path
from shutil import rmtree
from typing import Union
from decimal import Decimal
from io import BytesIO
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from azure.common import AzureException
from azure.storage.filedatalake import DataLakeServiceClient
from pandas import DataFrame
import pyarrow.fs
import pyarrow.parquet as pq
import pyarrowfs_adlgen2
from azure.common import AzureException
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.storage.filedatalake import DataLakeServiceClient
from behave.runner import Context
from openpyxl import load_workbook
from pandas import DataFrame
from pyspark.sql import Row
from pyspark.sql.types import _parse_datatype_string
from data_testing_package.common_methods.utilities import convert_string_type

def get_expected_results_parquetfile(file_path_in_repo: str) -> DataFrame:
    """Return parquet file as a DataFrame.

    Args:
        file_path_in_repo (string): file path of parquet file

    Raises:
        Exception: Error is the parquet file does not exist

    Returns:
        DataFrame: dataFrame of the parquet file contents
    """
    try:
        data = pq.read_table(file_path_in_repo).to_pandas()
        expected_value = pd.DataFrame(data)
    except Exception as exc:
        raise Exception("Failed to fetch the expected results file Local Repo") from exc
    return expected_value


def get_parquetfile_data_from_datalake(data_lake_service_client: DataLakeServiceClient, container: str, data_lake_file_path: str, local_file_path: Union[str, Path]) -> DataFrame:
    """Get parquet file contents from datalake and return as DataFrame.

    Args:
        data_lake_service_client: (DataLakeServiceClient) azure data lake service client
        container (str): Container name on Azure
        data_lake_file_path (str): File path the the parquet file on the Datalake
        local_file_path (str or Path): Location of the parquet file locally

    Returns:
        DataFrame: dataFrame of the parquet file contents
    """
    try:
        file_system_client = data_lake_service_client.get_file_system_client(container)
        paths = file_system_client.get_paths(data_lake_file_path)
        for path in paths:
            if "part-00000" in path.name:
                file_path = path.name
                file_client = data_lake_service_client.get_file_client(container, file_path)

                # needs to support both as some projects pass strings and some use path
                if isinstance(local_file_path, Path):
                    folder_path = local_file_path.parent.absolute()
                else:
                    folder_path = "/".join(str(local_file_path).split("/")[:-1])  # type: ignore

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                with open(local_file_path, "wb") as local_file:
                    download_file = file_client.download_file()
                    downloaded_bytes = download_file.readall()
                    local_file.write(downloaded_bytes)
                print("-----------------Parquet from datalake has been downloaded successfully-----------------")
                datalake_data = pq.read_table(local_file_path).to_pandas()
                return pd.DataFrame(datalake_data)
            else:
                print("No files to download")
    except AzureException as az_ex:
        print(az_ex)


def get_csv_data_from_datalake(data_lake_service_client: DataLakeServiceClient, container: str, data_lake_file_path: str, local_file_path: Union[Path, str]) -> DataFrame:
    """Get CSV file contents from datalake and return as DataFrame.

    Args:
        data_lake_service_client (DataLakeServiceClient): Azure DataLakeServiceClient
        container (str): Container name on Azure
        data_lake_file_path (str): File path the the CSV file on the Datalake
        local_file_path (str or Path): Location of the CSV file locally

    Returns:
        DataFrame: dataFrame of the CSV file contents
    """
    try:
        file_system_client = data_lake_service_client.get_file_system_client(container)
        paths = file_system_client.get_paths(data_lake_file_path)
        for path in paths:
            if ".csv" in path.name:
                file_path = path.name
                file_client = data_lake_service_client.get_file_client(container, file_path)

                # needs to support both as some projects pass strings and some use path
                if isinstance(local_file_path, Path):
                    folder_path = local_file_path.parent.absolute()
                else:
                    folder_path = "/".join(str(local_file_path).split("/")[:-1])  # type: ignore

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                with open(local_file_path, "w", encoding="utf-8") as local_file:
                    download_file = file_client.download_file()
                    downloaded_bytes = str(download_file.readall(), "utf-8").strip()
                    local_file.write(downloaded_bytes)
                    download_csv_dataframe = read_file_into_dataframe(local_file_path)  # type: ignore
                    print("-----------------CSV from datalake has been downloaded successfully-----------------")
                    return download_csv_dataframe
            else:
                print("No files to download")
    except AzureException as az_ex:
        raise Exception("Failed to Download csv file from Datalake") from az_ex


def dataframe_comparison(expected_value: DataFrame, actual_value: DataFrame) -> None:
    """Compare the contents of expected dataFrames (pandas).

    Args:
        expected_value (dataFrame): dataFrame of expected values
        actual_value (dataFrame): dateFrame of actual values from dataLake
    """
    result = pd.testing.assert_frame_equal(expected_value, actual_value, check_dtype=False, check_names=False)
    print(f"The comparison output is {result}")


def check_dataframes_are_equal(expected_value: DataFrame, actual_value: DataFrame) -> bool:
    """Numpy dataFrame comparison.

    Args:
        expected_value (dataFrame): dataFrame of expected values
        actual_value (dataFrame): dateFrame of actual values from dataLake

    Returns:
        bool: Returns a boolean value indicating if the comparison was successful
    """
    result = np.array_equal(expected_value.values, actual_value.values)
    print(f"The comparison output is {result}")
    return result


def remove_files_from_repo(local_file_path: str) -> bool:
    """Remove file from the local file system.

    Args:
        local_file_path (str): Location of the file to be removed
    Returns:
        bool: Returns a boolean value indicating if the removal was successful
    """
    try:
        os.remove(local_file_path)
    except OSError:
        print(f"No Parquet files present in {local_file_path}")
        pass
    else:
        print(f"Deleted Parquet file from {local_file_path}")
        return True
    return False


def read_file_into_dataframe(file_path_in_repo: Path) -> DataFrame:
    """Read a CSV file into a dataframe.

    Args:
        file_path_in_repo (Path): Path of the CSV file to convert to a dataframe

    Returns:
        DataFrame: dataFrame of the converted CSV file
    """
    df = pd.read_csv(Path(file_path_in_repo), header=0)
    return pd.DataFrame(df)


def remove_dir_and_files_within_it(path: str) -> None:
    # pylint: disable=W0703
    """Removes a directory and any files within it.

    Args:
        path: (str) the directory you want to remove
    """
    try:
        rmtree(path)
    except Exception as e:
        print(f"Unable to delete dir {path} \n Error: {e}")


def get_parquet_file_data_from_blob_storage(blob_service_client: BlobServiceClient, container: str, file_path: str, expected_file: str) -> DataFrame:
    """Get parquet file contents from blob storage and return as DataFrame.

    Args:
        blob_service_client: (BlobServiceClient) azure blob service client
        container (str): blob Container name on Azure
        file_path (str): File path the the parquet file on the Datalake
        expected_file (str): Expected file name to match

    Returns:
        DataFrame: dataFrame of the parquet file contents
    """
    container_client = blob_service_client.get_container_client(container)
    paths = [b.name for b in list(container_client.list_blobs(file_path))]
    for path in paths:
        check = path.split("/")
        if expected_file in check:
            if "part-00000" in path:
                file_path = path
                with BytesIO() as input_blob:
                    container_client.get_blob_client(file_path).download_blob().download_to_stream(input_blob)
                    input_blob.seek(0)
                    df = pd.read_parquet(input_blob)
                    return df
    raise FileNotFoundError(f"{expected_file} not found in {file_path} on {container}")


def load_parquet_file_data_from_datalake(data_lake_service_client: DataLakeServiceClient, container: str, data_lake_file_path: str, file_name: Union[str, Path]) -> DataFrame:
    """Load parquet file contents from datalake and return as DataFrame.

    Args:
        data_lake_service_client: (DataLakeServiceClient) azure data lake service client
        container (str): Container name on Azure
        data_lake_file_path (str): File path the the parquet file on the Datalake
        file_name (str or Path): Location of the parquet file locally

    Returns:
        DataFrame: dataFrame of the parquet file contents
    """
    try:
        file_system_client = data_lake_service_client.get_file_system_client(container)
        paths = file_system_client.get_paths(data_lake_file_path)
        for path in paths:
            check = path.name.split("/")
            if file_name in check:
                if "part-00000" in path.name:
                    file_path = path.name
                    file_client = data_lake_service_client.get_file_client(container, file_path)
                    data = file_client.download_file()
                    with BytesIO() as b:
                        data.readinto(b)
                        return pd.read_parquet(b)
    except AzureException as az_ex:
        print(az_ex)


def curated_schema_builder_from_dc(context: Context, parquet_folder_name: str) -> str:
    """Builds a PySpark schema string from the data catalogue based on the parquet_folder_name.

    Args:
        context (Context): Behave Context Object.
        parquet_folder_name (str): Name of the folder containing the parquet files to be checked.

    Returns:
        str: String representation of the PySpark schema
    """
    wb = load_workbook(context.data_catalogue_path)
    ws = wb["Data Journey"]
    all_rows = list(ws.rows)
    filtered_list = []
    # Pull information from specific cells.
    for row in all_rows:
        curated_object_name = row[13].value
        curated_attribute_name = row[14].value
        curated_data_type = row[16].value
        is_nullable = row[4].value
        if curated_object_name == parquet_folder_name:
            filtered_list.append([curated_object_name, curated_attribute_name, curated_data_type, is_nullable])
    remove_duplicates_from_list = set(tuple(x) for x in filtered_list)
    new_list = [list(x) for x in remove_duplicates_from_list]
    new_list.sort(key=lambda x: filtered_list.index(x))  # pylint: disable=W0108
    new_list.insert(-1, [parquet_folder_name, "IsCurrentFlag", "boolean", "N"])
    new_list.insert(-2, [parquet_folder_name, "IsDeletedFlag", "boolean", "N"])
    schema_str = ""
    for record in new_list:
        if record[3] == "Y":
            record[3] = ""
        else:
            record[3] = "not null"
        record.pop(0)
    schema_str = ", ".join([" ".join(record) for record in new_list])
    return schema_str


def create_parquet_file_from_json_data(context: Context, parquet_folder_name: str) -> None:
    """Creates a parquet file from a json file.

    Uses the schema_builder_from_dc function to build a PySpark schema string from the data catalogue based on the parquet_folder_name.

    Args:
        context (Context): Behave Context Object.
        parquet_folder_name (str): Name of the folder containing the parquet files to be checked.
    """

    def datetime_parser(json_dict: dict) -> dict:
        """Helper for json.loads to parse datetime strings to datetime.

        Args:
            json_dict (dict): Elements to be checked.

        Returns:
            dict: Updated json dictionary with valid datetime values
        """
        for key, value in json_dict.items():
            if isinstance(value, str):
                try:
                    json_dict[key] = convert_string_type(value)
                except (ValueError, AttributeError):
                    pass
        return json_dict

    schema = _parse_datatype_string(curated_schema_builder_from_dc(context, parquet_folder_name))
    parquet_folder_name = f"{context.static_json_for_parquet_comparison_folder}/curated/{parquet_folder_name}.json"
    if ".json" in parquet_folder_name:
        file_name = parquet_folder_name.split("/")[-1]
        parquet_folder_name = parquet_folder_name.replace(file_name, "")
    else:
        file_name = ".json"
    with open(f"{parquet_folder_name}/{file_name}", "r", encoding="utf-8") as j:
        data = json.loads(j.read(), parse_float=Decimal, object_hook=datetime_parser)
    json_records = data
    generated_df = context.spark.createDataFrame(data=[Row(**record) for record in json_records], schema=schema)
    return generated_df


def load_parquet_file_data_from_datalake_pyarrow(
    data_lake_service_client: DataLakeServiceClient, container: str, data_lake_file_path: str, file_name: Union[str, Path]
) -> DataFrame:
    """Load parquet file contents from datalake and return as DataFrame.

    This uses pyarrow and allows for partitioned parquet files to be loaded.

    Args:
        data_lake_service_client: (DataLakeServiceClient) azure data lake service client
        container (str): Container name on Azure
        data_lake_file_path (str): File path the the parquet file on the Datalake
        file_name (str or Path): Location of the parquet file locally

    Returns:
        DataFrame: dataFrame of the parquet file contents
    """
    try:
        file_system_client = data_lake_service_client.get_file_system_client(container)
        paths = file_system_client.get_paths(data_lake_file_path)
        for path in paths:
            check = path.name.split("/")
            if file_name in check:
                file_path = path.name
                handler = pyarrowfs_adlgen2.FilesystemHandler.from_account_name(file_system_client.account_name, container, DefaultAzureCredential())
                fs = pyarrow.fs.PyFileSystem(handler)
                dataset = pq.ParquetDataset(f"{file_path}/", filesystem=fs)
                df = dataset.read()
                return df.to_pandas()
    except AzureException as az_ex:
        print(az_ex)


def validate_columns(file1):
    """
    function to validate the schema of the dataframe
    Argument:
    file1: File to create dataframe
    """
    SCHEMA_COLS = ["firstName", "lastName", "email", "phoneNumber"]
    data_frame_1 = read_file_into_dataframe(file1)

    missing_cols = [col for col in SCHEMA_COLS if col not in data_frame_1.columns]
    if len(missing_cols) > 0:
        return False
    else:
        print("No header missing")
        return True
    
    
def remove_columns_from_df(file_name, cols_to_drop):
        """
        Removes the unwanted column from the dataframe
        Arguments:
        file_name: File columns need to be dropped from
        cols_to_drop: List of columns want to drop fromm the df
        """
        data_frame_1 = read_file_into_dataframe(file_name)
        df_dropped = data_frame_1.drop(columns=cols_to_drop, axis=1)
        for el in cols_to_drop:
            if el in df_dropped:
                return False
            else:
             return True
        