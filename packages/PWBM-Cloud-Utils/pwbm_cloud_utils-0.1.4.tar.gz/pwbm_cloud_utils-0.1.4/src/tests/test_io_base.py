"""
NOTE: In this module, parameterization prioritizes different target files.
Both cloud_base and local_base are included within a tuple inside the test function itself.
cloud_base and local_base are added to the parameterization list only when doing so does not result in duplication.
"""

import pytest
import os
from PWBM_Cloud_Utils.io_base import IOBase
from tests.helpers_testing import compare_path

LOCAL_BASE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'read')
CLOUD_BASE_PATH = "s3://cache-test1.pwbm-data/Testing Data/"


@pytest.fixture(params=[LOCAL_BASE_PATH, CLOUD_BASE_PATH])
def base_path(request):
    return request.param


class TestGetFileManager:

    """
    NOTE: Tests in this class follows the order of
    1. Test relative path
    2. Test absolute path
    3. Test errored conditions
    """

    # ---
    # test relative path
    # ---

    def test_get_file_manager(self, base_path):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action
        file_manager = io_base._get_file_manager("some_file")

        # Check
        assert file_manager.abspath == os.path.join(io_base.basepath, "some_file")

    # ---
    # test absolute path
    # ---

    def test_get_file_manager_abspath(self, base_path):
        # Setup
        io_base = IOBase(basepath=base_path)
        absolute_path = os.path.join(io_base.basepath, "some_file")

        # Action
        file_manager = io_base._get_file_manager(abspath=absolute_path)

        # Check
        assert file_manager.abspath == absolute_path

    # ---
    # test errored get_file_manager()
    # ---

    def test_errored_get_file_manager(self):
        """
        TODO: Junghoon is not sure whether it is realistic for basepath to be None.
        This should probably be an input validation, e.g. IOBase raises a value
        error if a invalid basepath is provided.
        """
        # Setup
        io_base = IOBase(basepath=None)

        # Action
        with pytest.raises(ValueError) as exc_info:
            io_base._get_file_manager()  # Neither path nor abspath provided

        # Check
        assert "No path or abspath set." in str(exc_info.value)


class TestCheckExtension:

    """
    NOTE: Tests in this class follows the order of
    1. Test files with valid extensions
    2. Test files without extensions
    3. Test files with invalid extensions
    """

    # ---
    # test files with valid extensions
    # ---

    @pytest.mark.parametrize("file_path, file_extension, expected_result", [
        ("parquet_df.parquet.tar", "tar", True),
        ("parquet_df.parquet.tar", "parquet", False),
        ("parquet_df.parquet.tar", "parquet.tar", True),
        ("pickle df.pkl.tar", r"pkl\.[a-zA-Z0-9]+", True),
    ])
    def test_file_with_extension(self, file_path, file_extension, expected_result, base_path):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action
        result = io_base.check_extension(file_path, file_extension)

        # Check
        assert result == expected_result

    # ---
    # test incorrect cases (without file extension)
    # ---

    @pytest.mark.parametrize("file_path, file_extension",[
        ("parquet_df parquet tar", "tar"),
        ("parquet_df parquet tar", "parquet"),
        ("parquet_df parquet tar", "parquet.tar"),
        ("partition_parquet", "parquet"),
        ("pickle df pkl tar", r"tar\.[a-zA-Z0-9]+"),
        ("pickle df pkl tar", r"\.tar\.[a-zA-Z0-9]+"),
    ])
    def test_file_without_extension(self, file_path, file_extension, base_path):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action
        result = io_base.check_extension(file_path, file_extension)

        # Check
        assert not result

    # ---
    # test incorrect cases (invalid extension)
    # ---

    @pytest.mark.parametrize("file_path, file_extension",[
        ("csv.csv1gzip", r"csv\.gzip"),
        ("csv.csv1gzip", "csv"),
        ("csv.csv1gzip", "gzip"),
        ("csv.csv1gzip", r"csv\.[a-zA-Z0-9]+")
    ])
    def test_file_invalid_extension(self, file_path, file_extension, base_path):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action
        result = io_base.check_extension(file_path, file_extension)

        # Check
        assert not result


class TestGetAbsolutePath:

    """
    NOTE: Tests in this class follows the order of
    1. Test correct cases
    2. Test correct cases override
    3. Test errored conditions
    """

    # ---
    # test get_absolute_path
    # ---

    @pytest.mark.parametrize("file_name", [
        ("some_file"),
        (".some_file")
    ])
    def test_get_absolute_path(self, base_path, file_name):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action
        path = io_base.get_absolute_path(file_name)

        # Check
        assert path == os.path.join(io_base.basepath, file_name)

    @pytest.mark.parametrize("file_name", [
        (""),
        (".")
    ])
    def test_get_absolute_path_root(self, base_path, file_name):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action
        path = io_base.get_absolute_path(file_name)

        # Check
        assert path == io_base.basepath

    # ---
    # test override get_absolute_path
    # ---

    def test_get_absolute_path_override(self, base_path):
        # Setup
        file_name = "some_file"
        io_base = IOBase(basepath=base_path)

        # Action
        path = io_base.get_absolute_path(file_name, basepath="OVERRIDE_BASEPATH")

        # Check
        assert path == os.path.join("OVERRIDE_BASEPATH", file_name)

    def test_get_absolute_path_override_root(self, base_path):
        # Setup
        file_name = ""
        io_base = IOBase(basepath=base_path)

        # Action
        path = io_base.get_absolute_path(file_name, basepath="OVERRIDE_BASEPATH")

        # Check
        assert path == "OVERRIDE_BASEPATH"

    # ---
    # test errored get_absolute_path()
    # ---

    def test_errored_get_absolute_path(self):
        """
        TODO: Junghoon is not sure whether it is realistic for basepath to be None.
        This should probably be an input validation, e.g. IOBase raises a value
        error if a invalid basepath is provided.
        """
        # Setup
        io_base = IOBase(basepath=None)

        # Action
        with pytest.raises(ValueError) as errormsg:
            IOBase.get_absolute_path(io_base, "data")

        # Check
        assert "No basepath set." in str(errormsg.value)


class TestListDirectory:

    """
    NOTE: Tests in this class follows the order of
    1. Test relative path
    2. Test absolute path
    3. Test errored conditions
    """

    # ---
    # test relative path
    # ---

    def test_list_directory_local(self):
        # Setup
        io_base = IOBase(basepath=LOCAL_BASE_PATH)

        # Action
        contents = io_base.list_directory("folder")

        # Check
        expected_path1 = os.path.normpath(io_base.get_absolute_path("folder/file1.txt"))
        expected_path2 = os.path.normpath(io_base.get_absolute_path("folder/file2.txt"))

        assert len(contents) == 2
        assert expected_path1 in contents
        assert expected_path2 in contents

    def test_list_directory_s3(self):
        # Setup
        io_base = IOBase(basepath=CLOUD_BASE_PATH)

        # Action
        contents = io_base.list_directory("folder")

        # Check
        expected_path1 = io_base.get_absolute_path("folder/file1.txt")
        expected_path2 = io_base.get_absolute_path("folder/file2.txt")

        assert len(contents) == 2
        assert expected_path1 in contents
        assert expected_path2 in contents

    # ---
    # test relative path (regex search)
    # ---

    def test_list_directory_regex_search_from_local_filesystem(self, base_path):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action
        contents = io_base.list_directory("folder", regex_search=r"2\.txt$")

        # Check:
        assert len(contents) == 1
        assert compare_path(contents[0], io_base.get_absolute_path("folder/file2.txt"))

    # ---
    # test absolute path
    # ---

    def test_list_directory_abspath_from_local_filesystem(self, base_path, tmp_path):
        # Setup:
        io_base = IOBase(basepath=base_path)
        abspath = os.path.join(str(tmp_path), "folder")
        os.makedirs(abspath)

        with open(os.path.join(abspath, "file.txt"), "w") as f:
            f.write("Hello World!")

        # Action:
        contents = io_base.list_directory(abspath=abspath)

        # Check:
        assert len(contents) == 1
        assert compare_path(contents[0], os.path.join(abspath, "file.txt"))

    # ---
    # test errored list_directory()
    # ---

    def test_list_directory_errors_from_local_filesystem(self, base_path):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action
        with pytest.raises(OSError) as errormsg:
            io_base.list_directory("does not exist directory")

        # Check
        assert "Directory does not exist" in str(errormsg.value)


class TestExists:

    """
    NOTE: Tests in this class follows the order of
    1. Test relative path
    2. Test absolute path
    3. Test errored conditions
    """

    # ---
    # test relative path
    # ---

    @pytest.mark.parametrize("target, is_folder", [
        # TODO: the behavior with empty strings is strange and this needs revision.
        #       Note that ("", False) also passes, which doesn't make logical sense
        #       even if we interpret ("", True) as checking whether the basepath
        #       directory exists.
        ("", True),  # Checks if basepath exists.
        ("folder", True),
        ("csv file.csv", False),
    ])
    def test_exists(self, base_path, target, is_folder):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action:
        exists = io_base.exists(target, is_folder=is_folder)

        # Check
        assert exists

    @pytest.mark.parametrize("target, is_folder", [
        ("does not exist.txt", False),
        ("does not exist", True),
    ])
    def test_not_exists_file_and_folder_from_local_filesystem(self, base_path, target, is_folder):
        # Setup
        io_base = IOBase(basepath=base_path)

        # Action:
        exists = io_base.exists(target, is_folder=is_folder)

        # Check:
        assert not exists

    # ---
    # test absolute path
    # ---

    @pytest.mark.parametrize("target, is_folder", [
        ("csv file.csv", False),
        ("", True),
    ])
    def test_exists_file_and_folder_abspath_from_local_filesystem(self, base_path, target, is_folder):
        # Setup
        io_base = IOBase(basepath=base_path)
        abspath = io_base.get_absolute_path(target) if target else io_base.basepath

        # Action:
        exists = io_base.exists(abspath=abspath, is_folder=is_folder)

        # Check:
        assert exists

    @pytest.mark.parametrize("target, is_folder", [
        ("does not exist.txt", False),
        ("does not exist", True)
    ])
    def test_not_exists_file_and_folder_abspath_from_local_filesystem(self, base_path, target, is_folder):
        # Setup
        io_base = IOBase(basepath=base_path)
        abspath = io_base.get_absolute_path(target)

        # Action:
        exists = io_base.exists(abspath=abspath, is_folder=is_folder)

        # Check:
        assert not exists
