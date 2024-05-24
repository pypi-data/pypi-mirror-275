"""
NOTE: Tests in each class follows the order of
1. Test relative path
2. Test relative path with other options
2. Test absolute path
3. Test decompression
5. Test errored conditions
"""

import pytest
import os
import gzip
import pandas as pd
import pickle
import filecmp

import PWBM_Cloud_Utils as utils
import botocore.exceptions
from tests.helpers_testing import compare_path

HTTP_NOT_FOUND = '404'
LOCAL_READ_BASEPATH = os.path.join(os.path.dirname(__file__), "data/read")


@pytest.fixture
def reader():

    os.environ["CLOUD_EXECUTION"] = "FALSE"
    reader = utils.IOReader(local_basepath="s3://cache-test1.pwbm-data/Testing Data/")

    yield reader

    os.environ.pop('CLOUD_EXECUTION', None)


class TestReadBytes:

    # ---
    # test relative path
    # ---

    @pytest.mark.parametrize("file_name", [
        "text file.txt",
        "image.jpeg"
    ])
    def test_read_bytes_from_s3_filesystem(self, reader, file_name):
        # Action:
        data = reader.read_bytes(file_name)

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, file_name), 'rb') as f:
            # TODO: there must be a better way than this.
            assert data.replace(b"\r\n", b"\n") == f.read().replace(b"\r\n", b"\n")

    # ---
    # test absolute path
    # ---

    @pytest.mark.parametrize("file_name", [
        "text file.txt",
        "image.jpeg"
    ])
    def test_read_bytes_abspath_from_s3_filesystem(self, reader, file_name):
        # Setup:
        abspath = reader.get_absolute_path(file_name)

        # Action:
        data = reader.read_bytes(abspath=abspath)

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, file_name), 'rb') as f:
            # TODO: there must be a better way than this.
            assert data.replace(b"\r\n", b"\n") == f.read().replace(b"\r\n", b"\n")

    # ---
    # test decompressioin
    # ---

    @pytest.mark.parametrize("file_name", [
        "text file.txt.gz",
        "image.tar.gz"
    ])
    def test_read_bytes_decompress_from_s3_filesystem(self, reader, file_name):
        # Action:
        data = reader.read_bytes(file_name, decompress=True)

        # Check:
        with gzip.open(os.path.join(LOCAL_READ_BASEPATH, file_name), 'rb') as f:
            assert data == f.read()

    # ---
    # test errored read_bytes()
    # ---

    def test_read_bytes_errors_from_s3_filesystem(self, reader):
        with pytest.raises(botocore.exceptions.ClientError) as errormsg:
            reader.read_bytes("does not exist.txt")
        assert errormsg.value.response['Error']['Code'] == HTTP_NOT_FOUND
        assert "Not Found" in errormsg.value.response['Error']['Message']


class TestRead:

    # ---
    # test relative path
    # ---

    def test_read_from_s3_filesystem(self, reader):
        # Action:
        data = reader.read("text file.txt")
        # Use Unix-style newline
        data = data.replace('\r\n', '\n')

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "text file.txt"), 'r') as f:
            assert data == f.read()

    # ---
    # test absolute path
    # ---

    def test_read_abspath_from_s3_filesystem(self, reader):
        # Setup:
        abspath = reader.get_absolute_path("text file.txt")

        # Action:
        data = reader.read(abspath=abspath)
        # Use Unix-style newline
        data = data.replace('\r\n', '\n')

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "text file.txt"), 'r') as f:
            assert data == f.read()

    # ---
    # test decompression
    # ---

    def test_read_decompress_from_s3_filesystem(self, reader):
        # Action:
        data = reader.read("text file.txt.gz", decompress=True)

        # Check:
        with gzip.open(os.path.join(LOCAL_READ_BASEPATH, "text file.txt.gz"), 'rb') as f:
            assert data == f.read().decode("utf-8")

    # ---
    # test errored read()
    # ---

    def test_read_errors_from_s3_filesystem(self, reader):
        with pytest.raises(botocore.exceptions.ClientError) as errormsg:
            reader.read("does not exist.txt")
        assert errormsg.value.response['Error']['Code'] == HTTP_NOT_FOUND


class TestReadPickle:

    # ---
    # test relative path
    # ---

    def test_read_pickle_from_s3_filesystem(self, reader):
        # Action:
        data = reader.read_pickle("pickle file.pkl")

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "pickle file.pkl"), 'rb') as f:
            assert data == pickle.loads(f.read())

    # ---
    # test absolute path
    # ---

    def test_read_pickle_abspath_from_s3_filesystem(self, reader):
        # Setup:
        abspath = reader.get_absolute_path("pickle file.pkl")

        # Action:
        data = reader.read_pickle(abspath=abspath)

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "pickle file.pkl"), 'rb') as f:
            assert data == pickle.loads(f.read())

    # ---
    # test decompression
    # ---

    def test_read_pickle_decompress_from_s3_filesystem(self, reader):
        # Action:
        data = reader.read_pickle("pickle file.pkl.gz", decompress=True)

        # Check:
        with gzip.open(os.path.join(LOCAL_READ_BASEPATH, "pickle file.pkl.gz"), 'rb') as f:
            assert data == pickle.loads(f.read())

    # ---
    # test errored read_pickle()
    # ---

    def test_read_pickle_errors_from_s3_filesystem(self, reader):
        with pytest.raises(botocore.exceptions.ClientError) as errormsg:
            reader.read_pickle("does not exist.pkl")
        assert errormsg.value.response['Error']['Code'] == HTTP_NOT_FOUND


class TestReadLines:

    # ---
    # test relative path
    # ---

    def test_read_lines_from_s3_filesystem(self, reader):
        # Action:
        data = reader.read_lines("csv file.csv")

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), 'r') as f:
            assert data == f.read().splitlines()

    # ---
    # test absolute path
    # ---

    def test_read_lines_abspath_from_s3_filesystem(self, reader):
        # Setup:
        abspath = reader.get_absolute_path("csv file.csv")

        # Action:
        data = reader.read_lines(abspath=abspath)

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), 'r') as f:
            assert data == f.read().splitlines()

    # ---
    # test decompression
    # ---

    def test_read_lines_decompress_from_s3_filesystem(self, reader):
        # Action:
        data = reader.read_lines("csv file.csv.gz", decompress=True)

        # Check:
        with gzip.open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv.gz"), 'rb') as f:
            assert data == [x.decode('utf-8') for x in f.read().splitlines()]

    # ---
    # test errored read_lines()
    # ---

    def test_read_lines_errors_from_s3_filesystem(self, reader):
        with pytest.raises(botocore.exceptions.ClientError) as errormsg:
            reader.read_lines("does not exist.csv")
        assert errormsg.value.response['Error']['Code'] == HTTP_NOT_FOUND


class TestReadDf:

    # ---
    # test relative path (with and without pandas args)
    # ---

    @pytest.mark.parametrize("file_name, file_type, read_method", [
        ("csv file.csv", "infer", pd.read_csv),
        ("pickle df.pkl", "infer", pd.read_pickle),
        ("parquet df.parquet", "infer", pd.read_parquet),
        ("parquet df.parquet.snappy", "infer", pd.read_parquet), # Note: OLG uses parquet.snappy files
        ("partition_parquet", "parquet", pd.read_parquet)
    ])
    def test_read_df_from_s3_filesystem(self, reader, file_name, file_type, read_method):
        # Action:
        df = reader.read_df(file_name, filetype = file_type)

        # Check:
        expected_df = read_method(os.path.join(LOCAL_READ_BASEPATH, file_name))

        assert df.equals(expected_df)

    # ---
    # test relative path (with pandas args)
    #
    # The following tests are not parametrized for the sake of readability
    # ---

    def test_read_df_csv_pandas_args_from_s3_filesystem(self, reader):
        # Action:
        pandas_args = {
            "index_col": 0
        }
        df = reader.read_df("csv file.csv", pandas_args=pandas_args)

        # Check:
        assert df.equals(pd.read_csv(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), index_col=0))

    def test_read_df_pickle_pandas_args_from_s3_filesystem(self, reader):
        # Action:
        pandas_args = {
            "compression": "tar"
        }
        df = reader.read_df("pickle df.pkl.tar", pandas_args=pandas_args)

        # Check:
        assert df.equals(pd.read_pickle(os.path.join(LOCAL_READ_BASEPATH, "pickle df.pkl.tar"), compression="tar"))

    def test_read_df_parquet_pandas_args_from_s3_filesystem(self, reader):
        # Action:
        pandas_args = {
            "engine": "pyarrow"
        }
        df = reader.read_df("parquet df.parquet", pandas_args=pandas_args)

        # Check:
        assert df.equals(pd.read_parquet(os.path.join(LOCAL_READ_BASEPATH, "parquet df.parquet")))

    def test_read_df_parquet_partition_filter_from_s3_filesystem(self, reader):
        # Action:
        pandas_args = {
            "filters": [("Year", ">", 2001), ("PersonID", "<=", 5)]
        }
        df = reader.read_df("partition_parquet", filetype="parquet", pandas_args=pandas_args)

        # Check:
        assert df.equals(pd.read_parquet(reader.get_absolute_path("partition_parquet"), filters=pandas_args["filters"]))

    # ---
    # test absolute path
    # ---

    @pytest.mark.parametrize("file_name, file_type, read_method", [
        ("csv file.csv", "infer", pd.read_csv),
        ("pickle df.pkl", "infer", pd.read_pickle),
        ("parquet df.parquet", "infer", pd.read_parquet),
        ("parquet df.parquet.snappy", "infer", pd.read_parquet), # Note: OLG uses parquet.snappy files
        ("partition_parquet", "parquet", pd.read_parquet)
    ])
    def test_read_df_abspath_from_s3_filesystem(self, reader, file_name, file_type, read_method):
        # Action
        abspath = reader.get_absolute_path(file_name)

        df = reader.read_df(abspath=abspath, filetype = file_type)

        # Check:
        assert df.equals(read_method(os.path.join(LOCAL_READ_BASEPATH, file_name)))

    # ---
    # test decompressioin
    #
    # The following 3 tests are not parametrized as read_parquet has no compression args.
    # ---

    def test_read_df_csv_decompress_from_s3_filesystem(self, reader):
        # Action:
        df = reader.read_df("csv file.csv.gz", decompress=True)

        # Check:
        assert df.equals(pd.read_csv(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv.gz"), compression="gzip"))

    def test_read_df_pickle_decompress_from_s3_filesystem(self, reader):
        # Action:
        df = reader.read_df("pickle df.pkl.gz", decompress=True)

        # Check:
        assert df.equals(pd.read_pickle(os.path.join(LOCAL_READ_BASEPATH, "pickle df.pkl.gz"), compression="gzip"))

    def test_read_df_parquet_decompress_from_s3_filesystem(self, reader):
        # Action:
        df = reader.read_df("parquet df.parquet.gz", decompress=True)

        # Check:
        assert df.equals(pd.read_parquet(os.path.join(LOCAL_READ_BASEPATH, "parquet df.parquet.gz")))

    # ---
    # test errored read_df()
    # ---

    def test_read_df_errors_from_s3_filesystem(self, reader):
        with pytest.raises(FileNotFoundError) as errormsg:
            reader.read_df("does not exist.csv")

        expected_error_msg = "cache-test1.pwbm-data/Testing Data/does not exist.csv"
        assert expected_error_msg in str(errormsg.value)


class TestReadfile:

    # ---
    # test relative path
    # ---

    def test_read_file_from_s3_filesystem(self, reader, tmp_path):
        # Action:
        reader.read_file(os.path.join(str(tmp_path), "csv file.csv"), "csv file.csv")

        # Check:
        with open(os.path.join(str(tmp_path), "csv file.csv"), 'r') as f_out:
            with open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), 'r') as f_in:
                assert f_in.read() == f_out.read()

    # ---
    # test absolute path
    # ---

    def test_read_file_abspath_from_s3_filesystem(self, reader, tmp_path):
        # Setup:
        abspath = reader.get_absolute_path("csv file.csv")

        # Action:
        reader.read_file(os.path.join(str(tmp_path), "csv file.csv"), abspath=abspath)

        # Check:
        with open(os.path.join(str(tmp_path), "csv file.csv"), 'r') as f_out:
            with open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), 'r') as f_in:
                assert f_in.read() == f_out.read()

    # ---
    # test decompression
    # ---

    def test_read_file_decompress_from_s3_filesystem(self, reader, tmp_path):
        # Action:
        reader.read_file(os.path.join(str(tmp_path), "csv file.csv"), "csv file.csv.gz", decompress=True)

        # Check:
        with open(os.path.join(str(tmp_path), "csv file.csv"), 'r') as f_out:
            with open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), 'r') as f_in:
                assert f_in.read() == f_out.read()

    # ---
    # test errored read_file()
    # ---

    def test_read_file_errors_from_s3_filesystem(self, reader):
        with pytest.raises(botocore.exceptions.ClientError) as errormsg:
            reader.read_file("errored file.csv", "does not exist.csv")

        assert errormsg.value.response['Error']['Code'] == HTTP_NOT_FOUND


class TestReadDirectory:

    # ---
    # test relative path
    # ---

    def test_read_directory_from_s3_filesystem(self, reader, tmp_path):
        # Action:
        reader.read_directory(str(tmp_path), "sub_folder")

        # Check:
        result = filecmp.dircmp(os.path.join(LOCAL_READ_BASEPATH, "folder"), str(tmp_path))

        assert len(result.common) == 2
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test absolute path
    # ---

    def test_read_directory_abspath_from_s3_filesystem(self, reader, tmp_path):
        # Setup:
        abspath = reader.get_absolute_path("sub_folder/")

        # Action:
        reader.read_directory(str(tmp_path), abspath=abspath)

        # Check:
        result = filecmp.dircmp(os.path.join(LOCAL_READ_BASEPATH, "folder"), str(tmp_path))

        assert len(result.common) == 2
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test errored read_directory()
    # ---

    def test_read_directory_errors_from_s3_filesystem(self, reader):
        # Check:
        with pytest.raises(OSError) as errormsg:
            reader.read_directory("errored file.csv", "does not exist.csv")
        assert "Source directory does not exist" in str(errormsg.value)


class TestReadZipDirectory:

    # ---
    # test relative path
    # ---

    @pytest.mark.parametrize("dir_name, format_archive", [
        ("zip_dir", ""),
        ("tar_dir", "tar")
    ])
    def test_read_zip_directory_zip_and_tar_from_s3_filesystem(self, reader, tmp_path, dir_name, format_archive):

        # Action:
        reader.read_zip_directory(str(tmp_path), dir_name, format_archive=format_archive)

        # Check:
        result = filecmp.dircmp(os.path.join(LOCAL_READ_BASEPATH, "folder"), str(tmp_path))
        
        assert len(result.common) == 2
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test absolute path
    # ---  

    @pytest.mark.parametrize("dir_name, format_archive", [
        ("zip_dir.zip", "zip"),
        ("tar_dir.tar", "tar")
    ])
    def test_read_zip_directory_zip_and_tar_abspath_from_s3_filesystem(self, reader, dir_name, format_archive, tmp_path):
        # Setup:
        abspath = reader.get_absolute_path(dir_name)

        # Action:
        reader.read_zip_directory(str(tmp_path), abspath=abspath, format_archive=format_archive)

        # Check:
        result = filecmp.dircmp(os.path.join(LOCAL_READ_BASEPATH, "folder"), str(tmp_path))

        assert len(result.common) == 2
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test errored read_zip_directory()
    # ---

    def test_read_zip_directory_errors_from_s3_filesystem(self, reader):
        with pytest.raises(OSError) as errormsg:
            reader.read_zip_directory("errored file", "does not exist.zip")
        assert "Source directory does not exist" in str(errormsg.value)


class TestReadCache:

    """
    NOTE: Reader and writer class contains 1 cache-related test,
    the test should not perform any actual action by setting
    CLOUD_EXECUTION=FALSE. It is placed here to triger simple case.
    Full tests for cache are kept in test_cache.py
    """

    def test_read_in_cache_from_local_filesystem(self, reader, tmp_path):
        # Action:
        reader.read_in_cache(str(tmp_path))

        # Nothing should happen if cloud_execution=False
        assert reader.cloud_cache_basepath is None


class TestReadListDirectory:

    """
    NOTE: Reader and writer class contains 2 tests for .list_directory(),
    for one simple case and one errored condition.
    Full tests for .list_directory() are kept in test_io_base.py
    """

    # ---
    # test relative path (with and without regex search)
    # ---

    def test_reader_list_directory_from_s3_filesystem(self, reader):
        # Action:
        contents = reader.list_directory("sub_folder")

        # Check:
        assert len(contents) == 2
        assert reader.get_absolute_path("sub_folder/file1.txt") in contents
        assert reader.get_absolute_path("sub_folder/file2.txt") in contents

    # ---
    # test errored list_directory()
    # ---

    def test_reader_list_directory_errors_from_s3_filesystem(self, reader):
        with pytest.raises(OSError) as errormsg: 
            reader.list_directory("does not exist directory")
        assert "Directory does not exist" in str(errormsg.value)


class TestExists:

    """
    NOTE: Reader and writer class contains 2 tests for .exists(),
    for one simple case and one errored condition.
    Full tests for .exists() are kept in test_io_base.py
    """

    # ---
    # test relative path
    # ---

    @pytest.mark.parametrize("target, is_folder", [
        # TODO: the behavior with empty strings is strange and this needs revision.
        #       Note that ("", False) also passes, which doesn't make logical sense
        #       even if we interpret ("", True) as checking whether the basepath
        #       directory exists.
        ("csv file.csv", False),
        ("sub_folder", True),
        ("", True),  # Checks if basepath exists.
    ])
    def test_reader_exists_file_and_folder_from_s3_filesystem(self, reader, target, is_folder):
        # Action:
        exists = reader.exists(target, is_folder=is_folder)

        # Check:
        assert exists


class TestPath:

    @classmethod
    def setup_class(cls):
        os.environ["CLOUD_EXECUTION"] = "TRUE"
        os.environ["CLOUD_READ_BASEPATH"] = "s3://cloud-bucket/read/"
        os.environ["CLOUD_WRITE_BASEPATH"] = "s3://cloud-bucket/write/"
        os.environ["LOCAL_READ_BASEPATH"] = "//hpc3-fs.wharton.upenn.edu/PWBM/"
        os.environ["LOCAL_WRITE_BASEPATH"] = "./tests/output"

    @classmethod
    def teardown_class(cls):
        os.environ.pop("CLOUD_EXECUTION", None)
        os.environ.pop("CLOUD_READ_BASEPATH", None)
        os.environ.pop("CLOUD_WRITE_BASEPATH", None)
        os.environ.pop("LOCAL_READ_BASEPATH", None)
        os.environ.pop("LOCAL_WRITE_BASEPATH", None)

    # ---
    # test basepath
    # ---

    def test_cloud_read_base_path_env(self):
        # Action
        reader = utils.IOReader()

        # Check
        assert compare_path(reader.basepath, "s3://cloud-bucket/read/")

    def test_cloud_read_base_path_override(self):
        # Action
        reader = utils.IOReader(cloud_basepath="s3://cloud-override/read/", local_basepath="s3://local-override/read/")

        # Check
        assert compare_path(reader.basepath, "s3://cloud-override/read/")

    # ---
    # test absolute path
    # ---

    def test_cloud_read_get_abspath(self):
        # Setup:
        reader = utils.IOReader(cloud_basepath="s3://cloud-bucket/read/")

        # Action:
        abspath = reader.get_absolute_path("file.txt")

        # Check:
        assert compare_path(reader.basepath, "s3://cloud-bucket/read")
        assert compare_path(abspath, "s3://cloud-bucket/read/file.txt")
