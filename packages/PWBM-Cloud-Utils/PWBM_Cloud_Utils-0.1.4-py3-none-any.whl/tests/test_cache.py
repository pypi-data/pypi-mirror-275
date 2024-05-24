import os
import pytest

import PWBM_Cloud_Utils as utils


@pytest.fixture()
def reader(tmp_path):
    """ setup any state specific to the execution of the given class (which
    usually contains tests).
    """
    os.environ["CLOUD_EXECUTION"] = "TRUE"
    os.environ["CLOUD_CACHE_BASEPATH"] = "s3://cache-test1.pwbm-data/test cloud cache/"
    os.environ["CLOUD_WRITE_BASEPATH"] = "s3://cache-test1.pwbm-data/Output/"

    reader = utils.IOReader(cloud_basepath="s3://cache-test1.pwbm-data/Testing Data/")
    local_cache = str(tmp_path)  

    yield reader, local_cache

    os.environ.pop('CLOUD_EXECUTION', None)
    os.environ.pop('CLOUD_CACHE_BASEPATH', None)
    os.environ.pop('CLOUD_WRITE_BASEPATH', None)


@pytest.fixture()
def writer(tmp_path):
    """ setup any state specific to the execution of the given class (which
    usually contains tests).
    """
    os.environ["CLOUD_EXECUTION"] = "TRUE"
    os.environ["CLOUD_CACHE_BASEPATH"] = "s3://cache-test1.pwbm-data/test cloud cache/"
    os.environ["CLOUD_WRITE_BASEPATH"] = "s3://cache-test1.pwbm-data/Output/"

    writer = utils.IOWriter()
    local_cache = str(tmp_path)

    yield writer, local_cache

    os.environ.pop('CLOUD_EXECUTION', None)
    os.environ.pop('CLOUD_CACHE_BASEPATH', None)
    os.environ.pop('CLOUD_WRITE_BASEPATH', None)


class TestCache:

    def test_read_in_cache_nonexistant_from_local_filesystem(self, reader):
        # Action:
        reader, local_cache = reader
        reader.read_in_cache(local_cache)

        assert reader.list_directory(abspath=local_cache) == []

    def test_write_out_cache_from_local_filesystem(self, writer):
        # Setup
        writer, local_cache = writer
        os.makedirs(local_cache, exist_ok=True)

        test_files = ['csv file.csv', 'text file.txt']
        src_folder = './src/tests/data/read'
        # Write test files to local_cache directory
        for files in test_files:
            src_path = os.path.join(src_folder, files)
            dst_path = os.path.join(local_cache, files)
            with open(src_path, 'rb') as f_in, open(dst_path, 'wb') as f_out:
                f_out.write(f_in.read())

        # Action
        writer.write_out_cache(local_cache)

        #Check
        for files in test_files:
            original_file = os.path.join(src_folder, files)
            cached_file = os.path.join(local_cache, files)
            with open(original_file, 'rb') as f_orig, open(cached_file, 'rb') as f_cache:
                assert f_orig.read() == f_cache.read()
