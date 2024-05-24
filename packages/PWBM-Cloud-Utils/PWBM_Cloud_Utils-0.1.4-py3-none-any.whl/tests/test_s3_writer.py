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
import pandas as pd
import filecmp
from datetime import datetime
import boto3


from PWBM_Cloud_Utils.io_reader import IOReader
from tests.data.Person import Person
import PWBM_Cloud_Utils as utils
from tests.helpers_testing import compare_path

HTTP_NOT_FOUND = '404'
LOCAL_READ_BASEPATH = os.path.join(os.path.dirname(__file__), "data/read")
TIMESTAMP = datetime.now().strftime("%Y%m%d%H%M%S")


@pytest.fixture()
def person_list():
    p1 = Person("Fetty", 12)
    p2 = Person("Skelly", 3)
    return [p1, p2]

@pytest.fixture
def csv_payload():
    return [
        "key,value",
        "firstComputationYear,1996",
        "lastComputationYear,2150",
        "bool,FALSE",
        "float,1.05",
        "some string,string value"
    ]


@pytest.fixture
def writer():
    os.environ["CLOUD_EXECUTION"] = "FALSE"
    writer = utils.IOWriter(local_basepath=f"s3://cache-test1.pwbm-data/Output_{TIMESTAMP}/")

    yield writer

    os.environ.pop('CLOUD_EXECUTION', None)
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket('cache-test1.pwbm-data')
    bucket.objects.filter(Prefix=f"Output_{TIMESTAMP}/").delete()


class TestWriteBytes:

    # ---
    # test relative path
    # ---

    @pytest.mark.parametrize("file_name", [
        "text file.txt",
        "image.jpeg"
    ])
    def test_write_bytes_to_s3_filesystem(self, writer, file_name):
        with open(os.path.join(LOCAL_READ_BASEPATH, file_name), 'rb') as f:
            data = f.read()

        # Action:
        writer.write_bytes(data, file_name)

        # Check:
        data_s3 = IOReader().read_bytes(abspath=writer.get_absolute_path(file_name))
        assert data == data_s3

    # ---
    # test absolute path
    # ---

    @pytest.mark.parametrize("file_name", [
        "text file.txt",
        "image.jpeg"
    ])
    def test_write_bytes_abspath_to_s3_filesystem(self, writer, file_name):
        # Setup:
        with open(os.path.join(LOCAL_READ_BASEPATH, file_name), 'rb') as f:
            data = f.read()

        abspath = writer.get_absolute_path(file_name)

        # Action:
        writer.write_bytes(data, abspath=abspath)

        # Check:
        data_s3 = IOReader().read_bytes(abspath=abspath)
        assert data == data_s3

    # ---
    # test decompression
    # ---

    @pytest.mark.parametrize("file_name, compressed_name", [
        ("text file.txt", "text file.txt.gz"),
        ("image.jpeg", "image.tar.gz")
    ])
    def test_write_bytes_compress_to_s3_filesystem(self, writer, file_name, compressed_name):
        # Setup:
        with open(os.path.join(LOCAL_READ_BASEPATH, file_name), 'rb') as f:
            data = f.read()

        # Action:
        writer.write_bytes(data, compressed_name, compress=True)

        # Check:
        data_s3 = IOReader().read_bytes(abspath=writer.get_absolute_path(compressed_name), decompress=True)
        assert data == data_s3

    # ---
    # test errored write_bytes()
    # ---

    def test_write_bytes_errors_to_s3_filesystem(self, writer):
        with pytest.raises(TypeError) as errormsg:
            writer.write_bytes("String rather than bytes", "errored file.txt")
        assert "a bytes-like object is required" in str(errormsg.value)


class TestWrite:

    # ---
    # test relative path
    # ---

    def test_write_to_s3_filesystem(self, writer):
        data = "Test data"

        # Action:
        writer.write(data, "text file.txt")

        # Check:
        data_s3 = IOReader().read(abspath=writer.get_absolute_path("text file.txt"))
        assert data == data_s3

    def test_write_to_s3_filesystem_multiline(self, writer):
        with open(os.path.join(LOCAL_READ_BASEPATH, "text file.txt"), 'r') as f:
            data = f.read()

        # Action:
        writer.write(data, "text file.txt")

        # Check:
        data_s3 = IOReader().read(abspath=writer.get_absolute_path("text file.txt"))
        assert data == data_s3

    # ---
    # test absolute path
    # ---

    def test_write_abspath_to_s3_filesystem(self, writer):
        # Setup:
        data = "Test data"

        abspath = writer.get_absolute_path("text file.txt")

        # Action:
        writer.write(data, abspath=abspath)

        # Check:
        data_s3 = IOReader().read(abspath=abspath)
        assert data == data_s3

    def test_write_abspath_to_s3_filesystem_multiline(self, writer):
        # Setup:
        with open(os.path.join(LOCAL_READ_BASEPATH, "text file.txt"), 'r') as f:
            data = f.read()

        abspath = writer.get_absolute_path("text file.txt")

        # Action:
        writer.write(data, abspath=abspath)

        # Check:
        data_s3 = IOReader().read(abspath=abspath)
        assert data == data_s3

    # ---
    # test decompression
    # ---

    def test_write_compress_to_s3_filesystem(self, writer):
        # Setup:
        with open(os.path.join(LOCAL_READ_BASEPATH, "text file.txt"), 'r') as f:
            data = f.read()

        # Action:
        writer.write(data, "text file.txt.gz", compress=True)

        # Check:
        data_s3 = IOReader().read(abspath=writer.get_absolute_path("text file.txt.gz"), decompress=True)
        assert data == data_s3

    # ---
    # test errored write()
    # ---

    def test_write_errors_to_s3_filesystem(self, writer):
        with pytest.raises(AttributeError) as errormsg:
            writer.write(b"bytes rather than string", "errored file.txt")
        assert "'bytes' object has no attribute 'encode" in str(errormsg.value)


class TestWritePickle:

    # ---
    # test relative path
    # ---

    def test_write_pickle_to_s3_filesystem(self, writer, person_list):
        # Action:
        writer.write_pickle(person_list, "pickle file.pkl")

        # Check:
        p_list_s3 = IOReader().read_pickle(abspath=writer.get_absolute_path("pickle file.pkl"))
        assert person_list == p_list_s3

    # ---
    # test absolute path
    # ---

    def test_write_pickle_abspath_to_s3_filesystem(self, writer, person_list):
        # Setup:
        abspath = writer.get_absolute_path("pickle file.pkl")

        # Action:
        writer.write_pickle(person_list, abspath=abspath)

        # Check:
        p_list_s3 = IOReader().read_pickle(abspath=abspath)
        assert person_list == p_list_s3

    # ---
    # test decompression
    # ---

    def test_write_pickle_compress_to_s3_filesystem(self, writer, person_list):
        # Action:
        writer.write_pickle(person_list, "pickle file.pkl.gz", compress=True)

        # Check:
        p_list_s3 = IOReader().read_pickle(abspath=writer.get_absolute_path("pickle file.pkl.gz"), decompress=True)
        assert person_list == p_list_s3


class TestWriteLines:

    # ---
    # test relative path
    # ---

    def test_write_lines_to_s3_filesystem(self, writer, csv_payload):
        # Action:
        writer.write_lines(csv_payload, "csv file.csv")

        # Check:
        csv_s3 = IOReader().read_lines(abspath=writer.get_absolute_path("csv file.csv"))
        assert csv_payload == csv_s3

    # ---
    # test absolute path
    # ---

    def test_write_lines_abspath_to_s3_filesystem(self, writer, csv_payload):
        abspath = writer.get_absolute_path("csv file.csv")

        # Action:
        writer.write_lines(csv_payload, abspath=abspath)

        # Check:
        csv_s3 = IOReader().read_lines(abspath=abspath)
        assert csv_payload == csv_s3

    # ---
    # test decompression
    # ---

    def test_write_lines_compress_to_s3_filesystem(self, writer, csv_payload):

        # Action:
        writer.write_lines(csv_payload, "csv file.csv.gz", compress=True)

        # Check:
        csv_s3 = IOReader().read_lines(abspath=writer.get_absolute_path("csv file.csv.gz"), decompress=True)
        assert csv_payload == csv_s3


class TestWriteDf:

    # ---
    # test relative path (without pandas args)
    # ---

    @pytest.mark.parametrize("file_name, read_method", [
        ("csv file.csv", pd.read_csv),
        ("pickle df.pkl", pd.read_pickle),
        ("parquet df.parquet", pd.read_parquet),
        ("parquet df.parquet.snappy", pd.read_parquet),
    ])
    def test_write_df_to_s3_filesystem(self, writer, file_name, read_method):
        # Setup:
        df = read_method(os.path.join(LOCAL_READ_BASEPATH, file_name))

        # Action:
        writer.write_df(df, file_name)

        # Check:
        assert df.equals(IOReader().read_df(abspath=writer.get_absolute_path(file_name)))

    # ---
    # test relative path (with pandas args)
    #
    # The following tests are not parametrized for the sake of readability
    # ---

    def test_write_df_csv_pandas_args_to_s3_filesystem(self, writer):
        # Setup:
        df = pd.read_csv(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"))
        
        # Action:
        pandas_args = {
            "sep": "\t"
        }
        writer.write_df(df, "tsv file.tsv", pandas_args=pandas_args, filetype="csv")

        # Check:
        assert df.equals(IOReader().read_df(abspath=writer.get_absolute_path("tsv file.tsv"),
                                            pandas_args=pandas_args, filetype="csv"))

    def test_write_df_pickle_pandas_args_to_s3_filesystem(self, writer):
        # Setup:
        df = pd.read_pickle(os.path.join(LOCAL_READ_BASEPATH, "pickle df.pkl"))

        # Action:
        pandas_args = {
            "compression": "tar"
        }
        writer.write_df(df, "pickle df.pkl.tar", pandas_args=pandas_args)

        # Check:
        assert df.equals(IOReader().read_df(abspath=writer.get_absolute_path("pickle df.pkl.tar"),
                                            pandas_args=pandas_args))

    def test_write_df_parquet_pandas_args_to_s3_filesystem(self, writer):
        # Setup:
        df = pd.read_parquet(os.path.join(LOCAL_READ_BASEPATH, "parquet df.parquet"))
  
        # Action
        pandas_args = {
            "engine": "pyarrow"
        }
        writer.write_df(df, "parquet df.parquet", pandas_args=pandas_args)

        # Check:
        assert df.equals(IOReader().read_df(abspath=writer.get_absolute_path("parquet df.parquet"), 
                                            pandas_args=pandas_args))

    def test_write_df_parquet_partition_to_s3_filesystem(self, writer):
        # Setup:
        pandas_args = {
            "partition_cols": ['Year']
        }
        df = pd.read_parquet(os.path.join(LOCAL_READ_BASEPATH, "partition_parquet"))

        # Action:
        writer.write_df(df, "partition_parquet", pandas_args=pandas_args, filetype="parquet")

        # Check:
        assert df.equals(pd.read_parquet(writer.get_absolute_path("partition_parquet")))

    # ---
    # test absolute path
    # ---

    @pytest.mark.parametrize("file_name, read_method", [
        ("csv file.csv", pd.read_csv),
        ("pickle df.pkl", pd.read_pickle),
        ("parquet df.parquet", pd.read_parquet),
        ("parquet df.parquet.snappy", pd.read_parquet),
    ])
    def test_write_df_abspath_to_s3_filesystem(self, writer, file_name, read_method):
        # Setup:
        df = read_method(os.path.join(LOCAL_READ_BASEPATH, file_name))
        abspath = writer.get_absolute_path(file_name)

        # Action:
        writer.write_df(df, abspath=abspath)

        # Check:
        assert df.equals(IOReader().read_df(abspath=abspath))

    # ---
    # test decompression
    # ---

    @pytest.mark.parametrize("file_name, read_method, output_file", [
        ("csv file.csv", pd.read_csv, "csv file.csv.gz"),
        ("parquet df.parquet", pd.read_parquet, "parquet df.parquet.gz"),
        ("pickle df.pkl", pd.read_pickle, "pickle df.pkl.gz")
    ])
    def test_write_df_compress_to_s3_filesystem(self, writer, file_name, read_method, output_file):
        # Setup:
        df = read_method(os.path.join(LOCAL_READ_BASEPATH, file_name))

        # Action:
        writer.write_df(df, output_file, compress=True)

        # Check:
        assert df.equals(IOReader().read_df(abspath=writer.get_absolute_path(output_file), decompress=True))

    # ---
    # test errored write_df
    # ---

    def test_write_df_errors_to_s3_filesystem(self, writer):
        with pytest.raises(AttributeError) as errormsg:
            writer.write_df("not a df", "errored file.csv")
        assert "'str' object has no attribute 'to_csv'" in str(errormsg.value)


class TestWriteFile:

    # ---
    # test relative path
    # ---

    def test_write_file_to_s3_filesystem(self, writer):
        # Action:
        writer.write_file(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), "csv file.csv")

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), 'rb') as f_in:
            assert f_in.read() == IOReader().read_bytes(abspath=writer.get_absolute_path("csv file.csv"))

    # ---
    # test absolute path
    # ---

    def test_write_file_abspath_to_s3_filesystem(self, writer):
        # Setup:
        abspath = writer.get_absolute_path("csv file.csv")

        # Action:
        writer.write_file(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), abspath=abspath)

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), 'rb') as f_in:
            assert f_in.read() == IOReader().read_bytes(abspath=abspath)

    # ---
    # test decompression
    # ---

    def test_write_file_compress_to_s3_filesystem(self, writer):
        # Action:
        writer.write_file(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), "csv file.csv.gz", compress=True)

        # Check:
        with open(os.path.join(LOCAL_READ_BASEPATH, "csv file.csv"), 'rb') as f_in:
            assert f_in.read() == IOReader().read_bytes(abspath=writer.get_absolute_path("csv file.csv.gz"), decompress=True)

    # ---
    # test errored write_file()
    # ---

    def test_write_file_errors_to_s3_filesystem(self, writer):
        with pytest.raises(FileNotFoundError) as errormsg:
            writer.write_file("file does not exist", "errored file.csv")
        assert "file does not exist" in str(errormsg.value)


class TestWriteDirectory:

    # ---
    # test relative path
    # ---

    def test_write_directory_to_s3_filesystem(self, writer, tmp_path):
        # Action:
        writer.write_directory(LOCAL_READ_BASEPATH, "directory")

        # Check:
        IOReader().read_directory(str(tmp_path), abspath=writer.get_absolute_path("directory"))

        result = filecmp.dircmp(LOCAL_READ_BASEPATH, str(tmp_path))

        assert len(result.common) == 19
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test absolute path
    # ---

    def test_write_directory_abspath_to_s3_filesystem(self, writer, tmp_path):
        # Setup:
        abspath = writer.get_absolute_path("sub_folder")

        # Action:
        writer.write_directory(os.path.join(LOCAL_READ_BASEPATH, "folder/"), abspath=abspath)

        # Check:
        IOReader().read_directory(str(tmp_path), abspath=abspath)

        result = filecmp.dircmp(os.path.join(LOCAL_READ_BASEPATH, "folder"), str(tmp_path))

        assert len(result.common) == 2
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test errored write_directory
    # ---

    def test_write_directory_errors_to_s3_filesystem(self, writer):
        with pytest.raises(OSError) as errormsg:
            writer.write_directory("file does not exist", "errored file.csv")
        assert "Source directory does not exist" in str(errormsg.value)


class TestWriteZipDirectory:

    # ---
    # test relative path
    # ---

    @pytest.mark.parametrize("directory_name, format_archive", [
        ("zip_dir", None),
        ("gztar_dir", "gztar")
    ])
    def test_write_zip_directory_to_s3_filesystem(self, writer, directory_name, format_archive, tmp_path):
        # Action:
        writer.write_zip_directory(LOCAL_READ_BASEPATH, directory_name, format_archive=format_archive)

        extension = ".zip" if format_archive is None else ""
        path = writer.get_absolute_path(f"{directory_name}{extension}")

        # Check
        IOReader().read_zip_directory(str(tmp_path), abspath=path, format_archive=format_archive)

        result = filecmp.dircmp(LOCAL_READ_BASEPATH, str(tmp_path))

        assert len(result.common) == 19
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test absolute path
    # ---

    @pytest.mark.parametrize("format_archive, extension", [
        ("zip", ".zip"),
        ("gztar", ".tar.gz")
    ])
    def test_write_directory_abspath_to_s3_filesystem(self, writer, tmp_path, format_archive, extension):
        # Setup:
        abspath = writer.get_absolute_path("sub_folder")
        
        # Action:
        writer.write_zip_directory(os.path.join(LOCAL_READ_BASEPATH, "folder"), abspath=abspath, format_archive=format_archive)

        # Check:
        IOReader().read_zip_directory(str(tmp_path), abspath=f"{abspath}{extension}", format_archive=format_archive)

        result = filecmp.dircmp(os.path.join(LOCAL_READ_BASEPATH, "folder"), str(tmp_path))

        assert len(result.common) == 2
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test errored write_zip_directory()
    # ---

    def test_write_zip_directory_errors_to_s3_filesystem(self, writer):
        with pytest.raises(OSError) as errormsg:
            writer.write_zip_directory("file does not exist", "errored file.csv")
        assert "Source directory does not exist" in str(errormsg.value)


class TestWriteCache:

    """
    NOTE: Reader and writer class contains 1 cache-related test,
    the test should not perform any actual action by setting
    CLOUD_EXECUTION=FALSE. It is placed here to triger simple case.
    Full tests for cache are kept in test_cache.py
    """

    def test_write_out_cache_from_local_filesystem(self, writer):
        # Action:
        writer.write_out_cache(LOCAL_READ_BASEPATH)

        # Nothing should happen if cloud_execution=False
        assert writer.cloud_cache_basepath is None


class TestWriteListDirectory:

    """
    NOTE: Reader and writer class contains 2 tests for .list_directory(),
    for one simple case and one errored condition.
    Full tests for .list_directory() are kept in test_io_base.py
    """

    # ---
    # test relative path
    # ---

    def test_write_list_directory_to_s3_filesystem(self, writer):
        # Setup:
        writer.write_bytes(b"Hello World!", "folder/text file.txt")

        # Action:
        contents = writer.list_directory("folder")

        # Check:
        assert len(contents) == 1
        assert contents[0] == writer.get_absolute_path("folder/text file.txt")

    # ---
    # test errored list_directory
    # ---

    def test_write_list_directory_errors_to_s3_filesystem(self, writer):
        with pytest.raises(TypeError) as errormsg:
            writer.list_directory(b"errored file.csv", "errored file.csv")
        assert "IOBase.list_directory() takes from 1 to 2 positional arguments but 3 were given" in str(errormsg.value)


class TestExists:

    """
    NOTE: Reader and writer class contains 2 tests for .list_directory(),
    for one simple case and one errored condition.
    Full tests for .exists() are kept in test_io_base.py
    """

    # ---
    # test relative path
    # ---

    def test_writer_exists_file_to_s3_filesystem(self, writer):
        # Setup:
        writer.write_bytes(b"Hello World!", "folder/text file.txt")

        # Action:
        exists = writer.exists("folder/text file.txt")

        # Check:
        assert exists

    # ---
    # test errored exists()
    # ---

    def test_writer_exists_errors_to_s3_filesystem(self, writer):
        with pytest.raises(TypeError) as errormsg:
            writer.exists(b"errored file.csv", "errored file.csv")
        assert "IOBase.exists() takes from 1 to 2 positional arguments but 3 were given" in str(errormsg.value)


class TestS3WriterPath:

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
    # test base path
    # ---

    def test_cloud_write_base_path_env(self):
        # Action
        writer = utils.IOWriter()

        # Check
        assert compare_path(writer.basepath, "s3://cloud-bucket/write/")

    # ---
    # test absolute path
    # ---

    def test_cloud_write_get_abspath(self):
        writer = utils.IOWriter()

        # Action:
        abspath = writer.get_absolute_path("sub/file.txt")

        # Check:
        assert compare_path(writer.basepath, "s3://cloud-bucket/write")
        assert compare_path(abspath, "s3://cloud-bucket/write/sub/file.txt")