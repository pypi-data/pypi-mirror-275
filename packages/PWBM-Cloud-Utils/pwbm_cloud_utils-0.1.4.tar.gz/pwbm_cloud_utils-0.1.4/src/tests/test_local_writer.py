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
import tarfile
from zipfile import ZipFile

from tests.data.Person import Person
import PWBM_Cloud_Utils as utils
from tests.helpers_testing import compare_path

LOCAL_READER_BASEPATH = os.path.join(os.path.dirname(__file__), 'data', 'read')


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
def writer(tmp_path):
    os.environ["CLOUD_EXECUTION"] = "FALSE"
    writer = utils.IOWriter(local_basepath=str(tmp_path))

    yield writer

    # Teardown
    os.environ.pop("CLOUD_EXECUTION", None)
    os.environ.pop("CLOUD_CACHE_BASEPATH", None)


class TestWriteBytes:

    # ---
    # test relative path
    # ---

    @pytest.mark.parametrize("file_name", [
        "text file.txt",
        "image.jpeg"
        ])
    def test_write_bytes_to_local_filesystem(self, file_name, writer):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, file_name)
        with open(path, 'rb') as f:
            data = f.read()

        # Action:
        writer.write_bytes(data, file_name)

        # Check:
        with open(writer.get_absolute_path(file_name), 'rb') as f:
            assert data == f.read()

    # ---
    # test absolute path
    # ---

    @pytest.mark.parametrize("file_name", [
        "text file.txt",
        "image.jpeg"
    ])
    def test_write_bytes_abspath_to_local_filesystem(self, writer, file_name):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, file_name)
        with open(path, 'rb') as f:
            data = f.read()

        abspath = writer.get_absolute_path(file_name)

        # Action:
        writer.write_bytes(data, abspath=abspath)

        # Check:
        with open(abspath, 'rb') as f:
            assert data == f.read()

    # ---
    # test decompression
    # ---

    @pytest.mark.parametrize("file_name, compressed_name", [
        ("text file.txt", "text file.txt.gz"),
        ("image.jpeg", "image.tar.gz")
    ])
    def test_write_bytes_compress_to_local_filesystem(self, writer, file_name, compressed_name):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, file_name)
        with open(path, 'rb') as f:
            data = f.read()

        # Action:
        writer.write_bytes(data, compressed_name, compress=True)

        # Check:
        with gzip.open(writer.get_absolute_path(compressed_name), 'rb') as f:
            assert data == f.read()

    # ---
    # test errored write_bytes()
    # ---

    def test_write_bytes_errors_to_local_filesystem(self, writer):
        with pytest.raises(TypeError) as errormsg:
            writer.write_bytes("String rather than bytes", "errored file.txt")
        assert "a bytes-like object is required" in str(errormsg.value)


class TestWrite:

    # ---
    # test relative path
    # ---

    def test_write_to_local_filesystem(self, writer):
        # Setup:
        data = "Test data"

        # Action:
        writer.write(data, "text file.txt")

        # Check:
        with open(writer.get_absolute_path("text file.txt"), 'r') as f:
            assert data == f.read()

    def test_write_to_local_filesystem_multiline(self, writer):
        # Setup:
        with open(os.path.join(LOCAL_READER_BASEPATH, "text file.txt"), 'r') as f:
            data = f.read()

        # Action:
        writer.write(data, "text file.txt")

        # Check:
        with open(writer.get_absolute_path("text file.txt"), 'r') as f:
            assert data == f.read()

    # ---
    # test absolute path
    # ---

    def test_write_abspath_to_local_filesystem(self, writer):
        # Setup:
        data = "Test data"
        abspath = writer.get_absolute_path("text file.txt")

        # Action:
        writer.write(data, abspath=abspath)

        # Check:
        with open(abspath,'r') as f:
            assert data == f.read()

    def test_write_abspath_to_local_filesystem_multiline(self, writer):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, "text file.txt")
        with open(path, 'r') as f:
            data = f.read()

        abspath = writer.get_absolute_path("text file.txt")

        # Action:
        writer.write(data, abspath=abspath)

        # Check:
        with open(abspath, 'r') as f:
            assert data == f.read()

    # ---
    # test decompression
    # ---

    def test_write_compress_to_local_filesystem(self, writer):
        # Setup:
        with open(os.path.join(LOCAL_READER_BASEPATH, "text file.txt"), 'r') as f:
            data = f.read()
        
        # Action:
        writer.write(data, "text file.txt.gz", compress=True)

        # Check:
        with gzip.open(writer.get_absolute_path("text file.txt.gz"), mode='rb') as f:
            # Note: gzip seems to always be giving bytes even if mode=r
            assert data == f.read().decode("utf-8")

    # ---
    # test errored write()
    # ---

    def test_write_errors_to_local_filesystem(self, writer):
        with pytest.raises(AttributeError) as errormsg:
            writer.write(b"bytes rather than string", "errored file.txt")
        assert "'bytes' object has no attribute 'encode'" in str(errormsg.value)


class TestWritePickle:

    # ---
    # test relative path
    # ---

    def test_write_pickle_to_local_filesystem(self, writer, person_list):
        # Setup:
        # Action:
        writer.write_pickle(person_list, "pickle file.pkl")

        # Check:
        with open(writer.get_absolute_path("pickle file.pkl"), 'rb') as f:
            assert person_list == pickle.loads(f.read())

    # ---
    # test absolute path
    # ---

    def test_write_pickle_abspath_to_local_filesystem(self, writer, person_list):
        # Setup:
        abspath = writer.get_absolute_path("pickle file.pkl")

        # Action:
        writer.write_pickle(person_list, abspath=abspath)

        # Check:
        with open(abspath, 'rb') as f:
            assert person_list == pickle.loads(f.read())

    # ---
    # test decompression
    # ---

    def test_write_pickle_compress_to_local_filesystem(self, writer, person_list):
        # Action:
        writer.write_pickle(person_list, "pickle file.pkl.gz", compress=True)

        # Check:
        with gzip.open(writer.get_absolute_path("pickle file.pkl.gz"), 'rb') as f:
            assert person_list == pickle.loads(f.read())


class TestWriteLines:

    # ---
    # test relative path
    # ---

    def test_write_lines_to_local_filesystem(self, csv_payload, writer):
        # Action:
        writer.write_lines(csv_payload, "csv file.csv")

        # Check:
        with open(writer.get_absolute_path("csv file.csv"), 'r') as f:
            assert csv_payload == f.read().splitlines()

    # ---
    # test absolute path
    # ---

    def test_write_lines_abspath_to_local_filesystem(self, csv_payload, writer):

        abspath = writer.get_absolute_path("csv file.csv")

        # Action:
        writer.write_lines(csv_payload, abspath=abspath)

        # Check:
        with open(abspath, 'r') as f:
            assert csv_payload == f.read().splitlines()

    # ---
    # test decompression
    # ---

    def test_write_lines_compress_to_local_filesystem(self, csv_payload, writer):
        # Action:
        writer.write_lines(csv_payload, "csv file.csv.gz", compress=True)

        # Check:
        with gzip.open(writer.get_absolute_path("csv file.csv.gz"), 'rb') as f:
            assert csv_payload == [x.decode('utf-8') for x in f.read().splitlines()]


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
    def test_write_df_to_local_filesystem(self, writer, file_name, read_method):
        # Setup:
        file_path = os.path.join(LOCAL_READER_BASEPATH, file_name)
        df = read_method(file_path)

        # Action:
        writer.write_df(df, file_name)

        # Check:
        assert df.equals(read_method(writer.get_absolute_path(file_name)))

    # ---
    # test relative path (with pandas args)
    #
    # The following tests are not parametrized for the sake of readability
    # ---

    def test_write_df_csv_pandas_args_to_local_filesystem(self, writer):
        # .tsv extension is intentionally used to check filetype= argument:
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, "csv file.csv")
        df = pd.read_csv(path)
        
        # Action:
        pandas_args = {
            "sep": "\t"
        }
        writer.write_df(df, "tsv file.tsv", pandas_args=pandas_args, filetype="csv")

        # Check:
        assert df.equals(pd.read_csv(writer.get_absolute_path("tsv file.tsv"), sep="\t"))

    def test_write_df_pickle_pandas_args_to_local_filesystem(self, writer):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, "pickle df.pkl")
        df = pd.read_pickle(path)
        
        # Action:
        pandas_args = {
            "compression": "tar"
        }
        writer.write_df(df, "pickle df.pkl.tar", pandas_args=pandas_args)

        # Check:
        assert df.equals(pd.read_pickle(writer.get_absolute_path("pickle df.pkl.tar"), compression="tar"))

    def test_read_df_parquet_pandas_args_from_local_filesystem(self, writer):
        # Setup
        path = os.path.join(LOCAL_READER_BASEPATH, "parquet df.parquet")
        df = pd.read_parquet(path)

        # Action:
        pandas_args = {
            "engine": "pyarrow"
        }
        writer.write_df(df, "parquet df.parquet.tar", pandas_args=pandas_args)

        # Check:
        assert df.equals(pd.read_parquet(writer.get_absolute_path("parquet df.parquet.tar")))

    def test_write_df_parquet_partition_to_local_filesystem(self, writer):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, "partition_parquet")
        df = pd.read_parquet(path)

        # Action:
        pandas_args = {
            "partition_cols": ['Year']
        }

        writer.write_df(df, "partition_parquet", filetype="parquet", pandas_args=pandas_args)

        # Check:
        assert df.equals(pd.read_parquet(writer.get_absolute_path("partition_parquet")))

    # ---
    # test abspath
    # ---

    @pytest.mark.parametrize("file_name, read_method", [
            ("csv file.csv", pd.read_csv),
            ("pickle df.pkl", pd.read_pickle),
            ("parquet df.parquet", pd.read_parquet),
            ("parquet df.parquet.snappy", pd.read_parquet),
    ])
    def test_write_df_abspath_to_local_filesystem(self, writer, file_name, read_method):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, file_name)
        df = read_method(path)

        abspath = writer.get_absolute_path(file_name)

        # Action:
        writer.write_df(df, abspath=abspath)

        # Check:
        assert df.equals(read_method(abspath))

    # ---
    # test decompression
    #
    # The following 3 tests are not parametrized as read_parquet has no compression args.
    # ---
    
    def test_write_df_parquet_compress_to_local_filesystem(self, writer):
        # Setup:
        df = pd.read_parquet(os.path.join(LOCAL_READER_BASEPATH, "parquet df.parquet"))

        # Action:
        writer.write_df(df, "parquet df.parquet.gz", compress=True)

        # Check:
        assert df.equals(pd.read_parquet(writer.get_absolute_path("parquet df.parquet.gz")))

    def test_write_df_csv_compress_to_local_filesystem(self, writer):
        # Setup:
        df = pd.read_csv(os.path.join(LOCAL_READER_BASEPATH, "csv file.csv"))

        # Action:
        writer.write_df(df, "csv file.csv.gz", compress=True)

        # Check:
        assert df.equals(pd.read_csv(writer.get_absolute_path("csv file.csv.gz"), compression="gzip"))

    def test_write_df_pickle_compress_to_local_filesystem(self, writer):
        # Setup:
        df = pd.read_pickle(os.path.join(LOCAL_READER_BASEPATH, "pickle df.pkl"))

        # Action:
        writer.write_df(df, "pickle df.pkl.gz", compress=True)

        # Check:
        assert df.equals(pd.read_pickle(writer.get_absolute_path("pickle df.pkl.gz"), compression="gzip"))

    # ---
    # test errored write_df()
    # ---

    def test_write_df_errors_to_local_filesystem(self, writer):
        with pytest.raises(AttributeError) as errormsg:
            writer.write_df("not a df", "errored file.csv")
        assert "'str' object has no attribute 'to_csv'" in str(errormsg.value)


class TestWriteFile:

    # ---
    # test relative path
    # ---

    def test_write_file_to_local_filesystem(self, writer):
        # Action:
        path = os.path.join(LOCAL_READER_BASEPATH, "csv file.csv")
        writer.write_file(path, "csv file.csv")

        # Check:
        with open(writer.get_absolute_path("csv file.csv"), 'r') as f_out:
            with open(path, 'r') as f_in:
                assert f_in.read() == f_out.read()

    # ---
    # test absolute path
    # ---

    def test_write_file_abspath_to_local_filesystem(self, writer):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, "csv file.csv")
        abspath = writer.get_absolute_path("csv file.csv")

        # Action:
        writer.write_file(path, abspath=abspath)

        # Check:
        with open(abspath, 'r') as f_out:
            with open(path, 'r') as f_in:
                assert f_in.read() == f_out.read()

    # ---
    # test decompression
    # ---

    def test_write_file_compress_to_local_filesystem(self, writer):
        # Action:
        path = os.path.join(LOCAL_READER_BASEPATH, "csv file.csv")
        writer.write_file(path, "csv file.csv.gz", compress=True)

        # Check:
        with gzip.open(writer.get_absolute_path("csv file.csv.gz"), 'rb') as f_out:
            with open(path, 'rb') as f_in:
                assert f_in.read() == f_out.read()

    # ---
    # test errored write_file()
    # ---

    def test_write_file_errors_to_local_filesystem(self, writer):
        with pytest.raises(FileNotFoundError) as errormsg:
            writer.write_file("file does not exist", "errored file.csv")
        assert "No such file or directory" in str(errormsg.value)


class TestWriteDirectory:

    # ---
    # test relative path
    # ---

    def test_write_directory_to_local_filesystem(self, writer):
        # Action:
        writer.write_directory(LOCAL_READER_BASEPATH, "directory")

        # Check:
        result = filecmp.dircmp(LOCAL_READER_BASEPATH,writer.get_absolute_path("directory"))

        assert len(result.common) == 19
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test absolute path
    # ---

    def test_write_directory_abspath_to_local_filesystem(self, writer):
        # Setup:
        abspath = writer.basepath

        # Action:
        writer.write_directory(LOCAL_READER_BASEPATH, abspath=abspath)

        # Check:
        result = filecmp.dircmp(LOCAL_READER_BASEPATH, abspath)

        assert len(result.common) == 19
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test errored write_directory()
    # ---

    def test_write_directory_errors_to_local_filesystem(self, writer):
        with pytest.raises(OSError) as errormsg:
            writer.write_directory("file does not exist", "errored file.csv")
        assert "Source directory does not exist" in str(errormsg.value)


class TestWriteZipDirectory:

    # ---
    # test relative path
    # ---

    @pytest.mark.parametrize("dir_name, format_archive", [
        ("zip_dir", "zip"), 
        ("gztar_dir", "gztar")
    ])
    def test_write_zip_directory_to_local_filesystem(self, writer, dir_name, format_archive):
        # Action:
        writer.write_zip_directory(LOCAL_READER_BASEPATH, dir_name, format_archive=format_archive)
        path = writer.get_absolute_path(dir_name)

        extract_path = os.path.join(os.path.dirname(path), 'extracted')
        os.makedirs(extract_path, exist_ok=True)

        # Extract gztar and zip
        if format_archive == "gztar":
            with tarfile.open(path + '.tar.gz', 'r:gz') as tar:
                tar.extractall(path=extract_path)
        else:
            with ZipFile(path + '.zip', 'r') as zip:
                zip.extractall(extract_path)

        # Check
        result = filecmp.dircmp(LOCAL_READER_BASEPATH, extract_path)

        assert len(result.common) == 19
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test absolute path
    # ---

    @pytest.mark.parametrize("dir_name, format_archive, extension", [
        ("zip_dir", "zip", ".zip"),
        ("gztar_dir", "gztar", ".tar.gz")
    ])
    def test_write_zip_directory_abspath_to_local_filesystem(self, writer, dir_name, format_archive, extension):
        # Action
        abspath = writer.get_absolute_path(dir_name)
        zip_dir = os.path.dirname(abspath)
        os.makedirs(zip_dir, exist_ok=True)

        writer.write_zip_directory(LOCAL_READER_BASEPATH, abspath=abspath, format_archive=format_archive)

        extract_path = os.path.join(zip_dir, 'extracted' + dir_name)
        os.makedirs(extract_path, exist_ok=True)

        # Extract gztar and zip
        if format_archive == "gztar":
            with tarfile.open(f"{abspath}{extension}", 'r:gz') as tar:
                tar.extractall(extract_path)
        else:
            with ZipFile(f"{abspath}{extension}", 'r') as zip:
                zip.extractall(extract_path)

        # Check
        result = filecmp.dircmp(LOCAL_READER_BASEPATH, extract_path)

        assert len(result.common) == 19
        assert len(result.left_only) == 0
        assert len(result.right_only) == 0
        assert len(result.diff_files) == 0

    # ---
    # test errored write_zip_directory
    # ---

    def test_write_zip_directory_errors_to_local_filesystem(self, writer):
        with pytest.raises(OSError) as errormsg:
            writer.write_zip_directory("file does not exist", "errored file.zip")
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
        writer.write_out_cache(LOCAL_READER_BASEPATH)

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

    def test_writer_list_directory_empty_to_local_filesystem(self, writer):
        # Setup:
        os.makedirs(writer.get_absolute_path("folder"))

        # Action:
        contents = writer.list_directory("folder")

        # Check:
        assert len(contents) == 0

    # ---
    # test errored list_directory()
    # ---

    def test_writer_list_directory_errors_to_local_filesystem(self, writer):
        with pytest.raises(TypeError) as errormsg:
            writer.list_directory(b"errored file.csv", "errored file.csv")
        assert "IOBase.list_directory() takes from 1 to 2 positional arguments but 3 were given" in str(errormsg.value)


class TestExists:

    """
    NOTE: Reader and writer class contains 2 tests for .exists(),
    for one simple case and one errored condition.
    Full tests for .exists() are kept in test_io_base.py
    """

    # ---
    # test relative path
    # ---

    def test_writer_exists_file_to_local_filesystem(self, writer):
        # Setup:
        path = os.path.join(LOCAL_READER_BASEPATH, "text file.txt")
        with open(path, 'rb') as f:
            data = f.read()

        writer.write_bytes(data, "text file.txt")

        # Action:
        exists = writer.exists("text file.txt")

        # Check:
        assert exists

    # ---
    # test errored exists()
    # ---

    def test_writer_exists_errors_to_local_filesystem(self, writer):
        with pytest.raises(TypeError) as errormsg:
            writer.exists(b"errored file.csv", "errored file.csv")
        assert "IOBase.exists() takes from 1 to 2 positional arguments but 3 were given" in str(errormsg.value)


class TestPath:

    @classmethod
    def setup_class(cls):
        os.environ["CLOUD_EXECUTION"] = "FALSE"
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

    def test_local_write_base_path_env(self):
        # Action
        writer = utils.IOWriter()

        # Check
        assert compare_path(writer.basepath, "./tests/output")

    def test_local_write_base_path_override(self):
        # Action
        writer = utils.IOWriter(local_basepath="s3://local-override/write/")

        # Check
        assert compare_path(writer.basepath, "s3://local-override/write/")

    # ---
    # test absolute path
    # ---

    def test_local_write_get_abspath(self):
        # Setup:
        writer = utils.IOWriter(local_basepath="./tests/data/write")

        # Action:
        abspath = writer.get_absolute_path("sub/file.txt")

        # Check:
        assert compare_path(writer.basepath, "./tests/data/write")
        assert compare_path(abspath, "./tests/data/write/sub/file.txt")