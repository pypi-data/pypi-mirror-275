import boto3
import io
import pytest
import os
import pandas as pd
import tempfile

from tests.data.Person import Person
from PWBM_Cloud_Utils.file_manager import S3FileManager
from tests.helpers_testing import compare_path

"""
NOTE: pytest in dev-packages of pipenv
"""
# @pytest.mark.skip
class TestS3FileManager:
    s3_read_basepath: str
    s3_write_basepath: str
    local_read_basepath: str
    local_write_basepath: str
    temp_dir: tempfile.TemporaryDirectory

    @classmethod
    def setup_class(self):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        self.s3_read_basepath = "s3://cache-test1.pwbm-data/Testing Data/"
        self.s3_write_basepath = "s3://cache-test1.pwbm-data/Output/"

        # create basepaths for building local paths
        self.local_read_basepath = "./src/tests/data/read"

        self.temp_dir = tempfile.TemporaryDirectory()
        self.local_write_basepath = self.temp_dir.name

    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
        self.temp_dir.cleanup()

        file_manager = S3FileManager(self.s3_write_basepath)

        if file_manager.exists(is_folder=True):
            delete_keys = []
            bucket_name = None
            for file_abspath in file_manager.list_directory():
                path_tuple = S3FileManager.parse_s3_path(file_abspath)

                if path_tuple.bucket != "" and path_tuple.path != "":
                    if bucket_name is None:
                        bucket_name = path_tuple.bucket

                    delete_keys.append({"Key": path_tuple.path})

            if bucket_name is not None:
                client = boto3.client("s3")
                client.delete_objects(Bucket=bucket_name, Delete={"Objects": delete_keys})

    def test_write_bytes_s3_file_manager(self):
        # Setup:
        with open(os.path.join(self.local_read_basepath, "text file.txt"), 'rb') as f_in:
            abspath = os.path.join(self.s3_write_basepath, "text file.txt")
            
            # Action:
            file_manager = S3FileManager(abspath)
            file_manager.write_bytes(f_in)

        # Check:
        with open(os.path.join(self.local_read_basepath, "text file.txt"), 'rb') as f_in:
            f_out = file_manager.read_bytes()
            
            assert f_in.read() == f_out.read()

    def test_read_bytes_from_s3_filesystem(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "text file.txt")

        # Action:
        file_manager = S3FileManager(abspath)
        stream = file_manager.read_bytes()

        # Check:
        with open(os.path.join(self.local_read_basepath, "text file.txt"), 'rb') as f:
            assert stream.read().replace(b"\r\n", b"\n") == f.read().replace(b"\r\n", b"\n")

    def test_write_bytes_bytesio_s3_file_manager(self):
        # Setup:
        with open(os.path.join(self.local_read_basepath, "text file.txt"), 'rb') as f_in:
            file_obj = io.BytesIO(f_in.read())

        file_obj.seek(0)

        abspath = os.path.join(self.s3_write_basepath, "text file.txt")
        
        # Action:
        file_manager = S3FileManager(abspath)
        file_manager.write_bytes(file_obj)

        # Check:
        with open(os.path.join(self.local_read_basepath, "text file.txt"), 'rb') as f_in:
            f_out = file_manager.read_bytes()
            
            assert f_in.read() == f_out.read()

    # Currently not working. I'm not sure how to fix because of the fact that folders don't actually exist in S3
    @pytest.mark.skip
    def test_list_directory_empty_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "empty")

        # Action:
        file_manager = S3FileManager(abspath)
        contents = list(file_manager.list_directory())

        # Check:
        assert len(contents) == 0

    def test_list_directory_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "sub_folder")

        # Action:
        file_manager = S3FileManager(abspath)
        contents = list(file_manager.list_directory())

        # Check:
        assert len(contents) == 2
        assert S3FileManager.normpath(os.path.join(abspath, "file1.txt")) in contents
        assert S3FileManager.normpath(os.path.join(abspath, "file2.txt")) in contents

    def test_list_directory_substring_search_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "sub_folder")

        # Action:
        file_manager = S3FileManager(abspath)
        contents = list(file_manager.list_directory(regex_search="file1"))

        # Check:
        assert len(contents) == 1
        assert compare_path(contents[0], os.path.join(abspath, "file1.txt"))

    def test_list_directory_regex_search_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "sub_folder")

        # Action:
        file_manager = S3FileManager(abspath)
        contents = list(file_manager.list_directory(regex_search="2.txt$"))

        # Check:
        assert len(contents) == 1
        assert compare_path(contents[0], os.path.join(abspath, "file2.txt"))

    def test_exists_file_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "text file.txt")

        # Action:
        file_manager = S3FileManager(abspath)
        exists = file_manager.exists()

        # Check:
        assert exists

    def test_not_exists_file_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "does not exist.txt")

        # Action:
        file_manager = S3FileManager(abspath)
        exists = file_manager.exists()

        # Check:
        assert not exists

    def test_exists_folder_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "sub_folder")

        # Action:
        file_manager = S3FileManager(abspath)
        exists = file_manager.exists(is_folder=True)

        # Check:
        assert exists

    def test_not_exists_folder_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "does not exist")

        # Action:
        file_manager = S3FileManager(abspath)
        exists = file_manager.exists(is_folder=True)

        # Check:
        assert not exists

    def test_exists_empty_folder_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "empty")

        # Action:f
        file_manager = S3FileManager(abspath)
        exists = file_manager.exists(is_folder=True)

        # Check:
        assert exists

    def test_normpath_s3_file_manager(self):
        # Setup:
        abspath = "mix/slash\\types"

        # Action:
        normpath = S3FileManager.normpath(abspath)

        # Check:
        assert normpath == abspath.replace("\\","/")

    def test_read_df_target_s3_file_manager(self):
        # Setup:
        abspath = os.path.join(self.s3_read_basepath, "pickle df.pkl")

        # Action:
        file_manager = S3FileManager(abspath)
        read_df_target = file_manager.read_df_target()

        # Check:
        assert read_df_target == S3FileManager.normpath(abspath)

    def test_write_df_pickle_s3_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "pickle df.pkl")
        write_abspath = os.path.join(self.s3_write_basepath, "pickle df.pkl")

        df = pd.read_pickle(read_abspath)

        # Action:
        file_manager = S3FileManager(write_abspath)
        file_manager.write_df(df.to_pickle)

        # Check:
        read_df_target = file_manager.read_df_target()
        df_write = pd.read_pickle(read_df_target)
        assert df.equals(df_write)

    def test_write_df_pickle_pandas_args_s3_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "pickle df.pkl")
        write_abspath = os.path.join(self.s3_write_basepath, "pickle df.pkl.tar")

        df = pd.read_pickle(read_abspath)

        pandas_args = {
            "compression": "tar"
        }

        # Action:
        file_manager = S3FileManager(write_abspath)
        file_manager.write_df(df.to_pickle, pandas_args=pandas_args)

        # Check:
        read_df_target = file_manager.read_df_target()
        df_write = pd.read_pickle(read_df_target, compression="tar")
        assert df.equals(df_write)
    
    def test_write_df_parquet_s3_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "parquet df.parquet")
        write_abspath = os.path.join(self.s3_write_basepath, "parquet df.parquet")

        df = pd.read_parquet(read_abspath)

        # Action:
        file_manager = S3FileManager(write_abspath)
        file_manager.write_df(df.to_parquet)

        # Check:
        read_df_target = file_manager.read_df_target()
        df_write = pd.read_parquet(read_df_target)
        assert df.equals(df_write)

    def test_write_df_parquet_pandas_args_s3_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "parquet df.parquet")
        write_abspath = os.path.join(self.s3_write_basepath, "parquet df.parquet")

        df = pd.read_parquet(read_abspath)

        pandas_args = {
            "index": False
        }

        # Action:
        file_manager = S3FileManager(write_abspath)
        file_manager.write_df(df.to_parquet, pandas_args=pandas_args)

        # Check:
        read_df_target = file_manager.read_df_target()
        df_write = pd.read_parquet(read_df_target)
        assert df.equals(df_write)

    # Note: currently works if run once, however it does not work on subsequent 
    # tests because deleting the S3 bucket is not working
    @pytest.mark.skip
    def test_write_df_parquet_partition_s3_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "partition_parquet")
        write_abspath = os.path.join(self.s3_write_basepath, "partition_parquet")

        df = pd.read_parquet(read_abspath)

        pandas_args = {
            "partition_cols": ['Year']
        }

        # Action:
        file_manager = S3FileManager(write_abspath)
        file_manager.write_df(df.to_parquet, pandas_args=pandas_args)

        # Check:
        df_write = pd.read_parquet(write_abspath)
        assert df.equals(df_write)
