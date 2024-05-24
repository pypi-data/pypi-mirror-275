import os

import PWBM_Cloud_Utils as utils
from tests.helpers_testing import compare_path


class TestConfig:

    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
        os.environ.pop('CLOUD_EXECUTION', None)
        os.environ.pop('CLOUD_READ_BASEPATH', None)
        os.environ.pop('CLOUD_WRITE_BASEPATH', None)
        os.environ.pop('LOCAL_READ_BASEPATH', None)
        os.environ.pop('LOCAL_WRITE_BASEPATH', None)
        os.environ.pop('CLOUD_CACHE_BASEPATH', None)

    def test_environ_var_exists_local(self):
        # Setup
        os.environ["CLOUD_EXECUTION"] = "FALSE"
        os.environ["CLOUD_READ_BASEPATH"] = "s3://cloud-bucket/read/"
        os.environ["CLOUD_WRITE_BASEPATH"] = "s3://cloud-bucket/write/"
        os.environ["LOCAL_READ_BASEPATH"] = "//hpc3-fs.wharton.upenn.edu/PWBM/"
        os.environ["LOCAL_WRITE_BASEPATH"] = "./tests/output"
        os.environ["CLOUD_CACHE_BASEPATH"] = "s3://cloud-bucket/cache/"

        # Action
        config = utils.IOConfig()

        # Check
        assert config.cloud_execution is False
        assert compare_path(str(config.cloud_read_basepath), "s3://cloud-bucket/read/")
        assert compare_path(str(config.cloud_write_basepath), "s3://cloud-bucket/write/")
        assert compare_path(str(config.local_read_basepath), "//hpc3-fs.wharton.upenn.edu/PWBM/")
        assert compare_path(str(config.local_write_basepath), "./tests/output")
        assert compare_path(str(config.cloud_cache_basepath), "s3://cloud-bucket/cache/")

    def test_environ_var_exists_cloud(self):
        # Setup
        os.environ["CLOUD_EXECUTION"] = "TRUE"
        os.environ["CLOUD_READ_BASEPATH"] = "s3://cloud-bucket/read/2/"
        os.environ["CLOUD_WRITE_BASEPATH"] = "s3://cloud-bucket/write/2/"
        os.environ["LOCAL_READ_BASEPATH"] = "//hpc3-fs.wharton.upenn.edu/PWBM/2/"
        os.environ["LOCAL_WRITE_BASEPATH"] = "./tests/output/2"
        os.environ["CLOUD_CACHE_BASEPATH"] = "s3://cloud-bucket/cache/2/"

        # Action
        config = utils.IOConfig()

        # Check
        assert config.cloud_execution is True
        assert compare_path(str(config.cloud_read_basepath), "s3://cloud-bucket/read/2")
        assert compare_path(str(config.cloud_write_basepath), "s3://cloud-bucket/write/2")
        assert compare_path(str(config.local_read_basepath), "//hpc3-fs.wharton.upenn.edu/PWBM/2")
        assert compare_path(str(config.local_write_basepath), "./tests/output/2")
        assert compare_path(str(config.cloud_cache_basepath), "s3://cloud-bucket/cache/2")

    def test_environ_var_not_set(self):
        # Setup
        os.environ.pop('CLOUD_EXECUTION', None)
        os.environ.pop('CLOUD_READ_BASEPATH', None)
        os.environ.pop('CLOUD_WRITE_BASEPATH', None)
        os.environ.pop('LOCAL_READ_BASEPATH', None)
        os.environ.pop('LOCAL_WRITE_BASEPATH', None)
        os.environ.pop('CLOUD_CACHE_BASEPATH', None)

        # Action
        config = utils.IOConfig()

        # Check
        assert config.cloud_execution is False
        assert config.cloud_read_basepath is None
        assert config.cloud_write_basepath is None
        assert config.local_read_basepath is None
        assert config.local_write_basepath is None
        assert config.cloud_cache_basepath is None
