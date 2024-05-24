import io
import pytest
import os
import shutil
import gzip
import pandas as pd
import pickle
import filecmp
import tempfile

from tests.data.Person import Person
from PWBM_Cloud_Utils.file_manager import LocalFileManager
from tests.helpers_testing import compare_path

"""
NOTE: pytest in dev-packages of pipenv
"""
# @pytest.mark.skip
class TestLocalFileManager:
    local_read_basepath: str
    local_write_basepath: str
    temp_dir: tempfile.TemporaryDirectory

    @classmethod
    def setup_class(self):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        # create basepaths for building local paths
        self.local_read_basepath = "./src/tests/data/read"

        self.temp_dir = tempfile.TemporaryDirectory()
        self.local_write_basepath = self.temp_dir.name

    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
        self.temp_dir.cleanup()

    def test_write_bytes_local_file_manager(self):
        # Setup:
        with open(os.path.join(self.local_read_basepath, "text file.txt"), 'rb') as f_in:
            abspath = os.path.join(self.local_write_basepath, "text file.txt")
            
            # Action:
            file_manager = LocalFileManager(abspath)
            file_manager.write_bytes(f_in)

            # Check:
            f_in.seek(0)
            with open(abspath, 'rb') as f_out:
                assert f_in.read() == f_out.read()

    def test_read_bytes_from_local_filesystem(self):
        # Setup:
        abspath = os.path.join(self.local_read_basepath, "text file.txt")

        # Action:
        file_manager = LocalFileManager(abspath)
        stream = file_manager.read_bytes()

        # Check:
        with open(abspath, 'rb') as f:
            assert stream.read() == f.read()

    def test_write_bytes_bytesio_local_file_manager(self):
        # Setup:
        with open(os.path.join(self.local_read_basepath, "text file.txt"), 'rb') as f_in:
            file_obj = io.BytesIO(f_in.read())

        file_obj.seek(0)

        abspath = os.path.join(self.local_write_basepath, "text file.txt")
        
        # Action:
        file_manager = LocalFileManager(abspath)
        file_manager.write_bytes(file_obj)

        # Check:
        with open(abspath, 'rb') as f_out:
            assert file_obj.getvalue() == f_out.read()

    def test_list_directory_empty_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_write_basepath, "folder")
        os.makedirs(abspath)

        # Action:
        file_manager = LocalFileManager(abspath)
        contents = list(file_manager.list_directory())

        # Check:
        assert len(contents) == 0

    def test_list_directory_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_read_basepath, "folder")

        # Action:
        file_manager = LocalFileManager(abspath)
        contents = list(file_manager.list_directory())

        # Check:
        assert len(contents) == 2
        assert LocalFileManager.normpath(os.path.join(abspath, "file1.txt")) in contents
        assert LocalFileManager.normpath(os.path.join(abspath, "file2.txt")) in contents

    def test_list_directory_regex_search_substring_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_write_basepath, "folder")
        os.makedirs(abspath)

        with open(os.path.join(abspath, "file.txt"), "w") as f:
            f.write("Hello World!")

        with open(os.path.join(abspath, "other.txt"), "w") as f:
            f.write("Goodbye World!")

        # Action:
        file_manager = LocalFileManager(abspath)
        contents = list(file_manager.list_directory(regex_search="file"))

        # Check:
        assert len(contents) == 1
        assert compare_path(contents[0], os.path.join(abspath, "file.txt"))

    def test_list_directory_regex_search_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_read_basepath, "folder")

        # Action:
        file_manager = LocalFileManager(abspath)
        contents = list(file_manager.list_directory(regex_search="2.txt$"))

        # Check:
        assert len(contents) == 1
        assert compare_path(contents[0], os.path.join(abspath, "file2.txt"))

    def test_exists_file_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_read_basepath, "text file.txt")

        # Action:
        file_manager = LocalFileManager(abspath)
        exists = file_manager.exists()

        # Check:
        assert exists

    def test_not_exists_file_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_read_basepath, "does not exist.txt")

        # Action:
        file_manager = LocalFileManager(abspath)
        exists = file_manager.exists()

        # Check:
        assert not exists

    def test_exists_folder_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_read_basepath, "folder")

        # Action:
        file_manager = LocalFileManager(abspath)
        exists = file_manager.exists(True)

        # Check:
        assert exists

    def test_not_exists_folder_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_read_basepath, "does not exist")

        # Action:
        file_manager = LocalFileManager(abspath)
        exists = file_manager.exists(True)

        # Check:
        assert not exists

    def test_exists_empty_folder_local_file_manager(self):
        # Setup:
        os.makedirs(self.local_write_basepath)
        abspath = self.local_write_basepath

        # Action:
        file_manager = LocalFileManager(abspath)
        exists = file_manager.exists(True)

        # Check:
        assert exists

    def test_normpath_local_file_manager(self):
        # Setup:
        abspath = "mix/slash\\types"

        # Action:
        normpath = LocalFileManager.normpath(abspath)

        # Check:
        assert normpath == os.path.normpath(abspath)

    def test_read_df_target_local_file_manager(self):
        # Setup:
        abspath = os.path.join(self.local_read_basepath, "pickle df.pkl")

        # Action:
        file_manager = LocalFileManager(abspath)
        read_df_target = file_manager.read_df_target()

        # Check:
        assert read_df_target == LocalFileManager.normpath(abspath)

    def test_write_df_pickle_local_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "pickle df.pkl")
        write_abspath = os.path.join(self.local_write_basepath, "pickle df.pkl")

        df = pd.read_pickle(read_abspath)

        # Action:
        file_manager = LocalFileManager(write_abspath)
        file_manager.write_df(df.to_pickle)

        # Check:
        df_write = pd.read_pickle(write_abspath)
        assert df.equals(df_write)

    def test_write_df_pickle_pandas_args_local_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "pickle df.pkl")
        write_abspath = os.path.join(self.local_write_basepath, "pickle df.pkl.tar")

        df = pd.read_pickle(read_abspath)

        pandas_args = {
            "compression": "tar"
        }

        # Action:
        file_manager = LocalFileManager(write_abspath)
        file_manager.write_df(df.to_pickle, pandas_args=pandas_args)

        # Check:
        df_write = pd.read_pickle(write_abspath, compression="tar")
        assert df.equals(df_write)
    
    def test_write_df_parquet_local_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "parquet df.parquet")
        write_abspath = os.path.join(self.local_write_basepath, "parquet df.parquet")

        df = pd.read_parquet(read_abspath)

        # Action:
        file_manager = LocalFileManager(write_abspath)
        file_manager.write_df(df.to_parquet)

        # Check:
        df_write = pd.read_parquet(write_abspath)
        assert df.equals(df_write)

    def test_write_df_parquet_pandas_args_local_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "parquet df.parquet")
        write_abspath = os.path.join(self.local_write_basepath, "parquet df.parquet")

        df = pd.read_parquet(read_abspath)

        pandas_args = {
            "engine": "pyarrow"
        }

        # Action:
        file_manager = LocalFileManager(write_abspath)
        file_manager.write_df(df.to_parquet, pandas_args=pandas_args)

        # Check:
        df_write = pd.read_parquet(write_abspath)
        assert df.equals(df_write)

    def test_write_df_parquet_partition_local_file_manager(self):
        # Setup:
        read_abspath = os.path.join(self.local_read_basepath, "partition_parquet")
        write_abspath = os.path.join(self.local_write_basepath, "partition_parquet")

        df = pd.read_parquet(read_abspath)

        pandas_args = {
            "partition_cols": ['Year']
        }

        # Action:
        file_manager = LocalFileManager(write_abspath)
        file_manager.write_df(df.to_parquet, pandas_args=pandas_args)

        # Check:
        df_write = pd.read_parquet(write_abspath)
        assert df.equals(df_write)

