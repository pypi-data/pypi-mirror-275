import os
import sys
import tarfile
import zipfile
from typing import Any
import botocore
import gzip
import pickle
import pandas as pd

from .io_base import IOBase
from .io_config import IOConfig

class IOReader(IOBase):
    def __init__(
        self, 
        cloud_basepath: str | None = None,
        local_basepath: str | None = None,
    ) -> None:
        """
        Constructor for IOReader. IOReader allows you to read files from either the 
        cloud_baspath location or the local_basepath, depending on where your code is executing. 
        By default, the basepaths defined in your .env file will be used but you can override 
        those using the constructor arguments.
    
        Attributes:
            cloud_basepath: basepath to use with reader when executing on the cloud.
            local_basepath: basepath to use with reader when executing locally.
        
        """
        config = IOConfig()
        self.cloud_execution = config.cloud_execution

        if config.cloud_execution:
            self.basepath = cloud_basepath
            self.cloud_cache_basepath = config.cloud_cache_basepath
            if self.basepath is None:
                self.basepath = config.cloud_read_basepath
        else:
            self.basepath = local_basepath
            self.cloud_cache_basepath = None
            if self.basepath is None:
                self.basepath = config.local_read_basepath
    
    def read_bytes(
        self, 
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        decompress: bool = False,
    ) -> bytes:
        """
        Read file specified by path or abspath and return its contents as a byte string.
    
        Attributes:
            path: Relative path to the file from within the IOReader's basepath directory, 
                  including file name and extension. path ignored if abspath specified, 
                  so either specify path or abspath not both. Positional only.
            abspath: Absolute path to the file, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored 
                     if abspath specified, so either specify path or abspath not both. 
                     Keyword only.
            decompress: Whether to decompress file using gzip. By default, False. Keyword only.
        
        Returns:
            bytes: byte string of file contents.
        """

        file_manager = self._get_file_manager(path, abspath=abspath)

        file_obj = file_manager.read_bytes()

        response = file_obj.read()
        file_obj.close()

        if decompress:
            response = gzip.decompress(response)
        
        return response

    def read(
        self, 
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        decompress: bool = False, 
    ) -> str:
        """
        Read file specified by path or abspath and return its contents as a string.

        Attributes:
            path: Relative path to the file from within the IOReader's basepath directory, 
                  including file name and extension. path ignored if abspath specified, 
                  so either specify path or abspath not both. Positional only.
            abspath: Absolute path to the file, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored 
                     if abspath specified, so either specify path or abspath not both. 
                     Keyword only.
            decompress: Whether to decompress file using gzip. By default, False. Keyword only.
        
        Returns:
            str: string of file contents.
        """
        return self.read_bytes(
            path, 
            abspath=abspath,
            decompress=decompress,
        ).decode("utf-8")

    def read_lines(
        self, 
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        decompress: bool = False, 
    ) -> list[str]:
        """
        Read file specified by path or abspath and return its contents as a list of 
        strings with one entry per line.

        Attributes:
            path: Relative path to the file from within the IOReader's basepath directory, 
                  including file name and extension. path ignored if abspath specified, 
                  so either specify path or abspath not both. Positional only.
            abspath: Absolute path to the file, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored 
                     if abspath specified, so either specify path or abspath not both. 
                     Keyword only.
            decompress: Whether to decompress file using gzip. By default, False. Keyword only.
        
        Returns:
            list[str]: list of strings with one entry per line of file contents.
        """
        return self.read(
            path, 
            abspath=abspath,
            decompress=decompress,
        ).splitlines()
        
    def read_pickle(
        self, 
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        decompress: bool = False, 
    ) -> Any:
        """
        Read pickle file specified by path or abspath and return its unpickled contents. 
        Note: if contents is a pandas Dataframe, please use read_df.
    
        Attributes:
            path: Relative path to the file from within the IOReader's basepath directory, 
                  including file name and extension. path ignored if abspath specified, 
                  so either specify path or abspath not both. Positional only.
            abspath: Absolute path to the file, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored 
                     if abspath specified, so either specify path or abspath not both. 
                     Keyword only.
            decompress: Whether to decompress file using gzip. By default, False. Keyword only.
        
        Returns:
            Any: unpickled file contents.
        """
        response = self.read_bytes(
            path, 
            abspath=abspath,
            decompress=decompress,
        )
        return pickle.loads(response)

    def read_df(
        self, 
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        decompress: bool = False, 
        filetype: str = "infer",
        pandas_args: dict | None = None
    ) -> pd.DataFrame:
        """
        Read file specified by path or abspath and return its contents as a pandas Dataframe. 
        File type automatically determined from path. Note: only csv, pickle, and parquet files supported. 
        If another file type needed, please use read_bytes or read_file.
    
        Attributes:
            path: Relative path to the file from within the IOReader's basepath directory, 
                  including file name and extension. path ignored if abspath specified, 
                  so either specify path or abspath not both. Positional only.
            abspath: Absolute path to the file, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored 
                     if abspath specified, so either specify path or abspath not both. 
                     Keyword only.
            decompress: Whether to decompress file using gzip. By default, False. Keyword only.
            filetype: File type of file being read. Possible values are: "csv", "pickle", "parquet", 
                      and "infer". Defaults to "infer", which means type is inferred from the path. 
                      Keyword only.
            pandas_args: A dictionary of arguments to add when calling pandas function. Defaults to {}. 
                         Keyword only.
        
        Returns:
            pd.DataFrame: file contents as a pandas Dataframe.
        """
        if pandas_args is None:
            pd_args = {}
        else:
            pd_args = pandas_args.copy()

        if abspath is None:
            if path is None:
                raise ValueError("No path or abspath set.")
            # uses config to build full absolute path
            abspath = self.get_absolute_path(path)

        file_manager = self._get_file_manager(abspath=abspath)

        response = file_manager.read_df_target()

        if filetype == "pickle" or (
            filetype == "infer" and (
                IOReader.check_extension(abspath, "pkl") or
                IOReader.check_extension(abspath, r"pkl\.[a-zA-Z0-9]+")
                
            )
        ):
            if decompress or IOReader.check_extension(abspath, "gz"):
                pd_args["compression"] = "gzip"

            return pd.read_pickle(response, **pd_args)
        
        elif filetype == "parquet" or (
            filetype == "infer" and (
                IOReader.check_extension(abspath, "parquet") or
                IOReader.check_extension(abspath, r"parquet\.[a-zA-Z0-9]+") or
                IOReader.check_extension(abspath, "pqt") or
                IOReader.check_extension(abspath, r"pqt\.[a-zA-Z0-9]+")
            )
        ):
            
            return pd.read_parquet(response, **pd_args)

        elif filetype == "csv" or (
            filetype == "infer" and (
                IOReader.check_extension(abspath, "csv") or
                IOReader.check_extension(abspath, r"csv\.[a-zA-Z0-9]+")
            )
        ):
            if decompress or IOReader.check_extension(abspath, "gz"):
                pd_args["compression"] = "gzip"

            return pd.read_csv(response, **pd_args)

        else:
            raise ValueError(
                "Invalid filetype. only csv, pickle, and parquet supported. "
                "Try read file or read bytes or explicitly setting filetype."
            )

    def read_file(
        self, 
        dest_path: str,
        src_path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        decompress: bool = False, 
    ) -> None:
        """
        Read file specified by src_path or abspath and write it to the dest_path.

        Attributes:
            dest_path: Absolute destination path to read the file to, including file name 
                       and extension. Positional only.
            src_path: Relative path to the source file from within the IOReader's basepath 
                      directory, including file name and extension. src_path ignored if abspath 
                      specified, so either specify src_path or abspath not both. Positional only.
            abspath: Absolute path to the source file, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". src_path ignored if 
                     abspath specified, so either specify src_path or abspath not both. 
                     Keyword only.
            decompress: Whether to decompress file using gzip. By default, False. Keyword only.
        """

        file_bytes = self.read_bytes(
            src_path, 
            abspath=abspath,
            decompress=decompress,
        )

        if not os.path.exists(os.path.dirname(dest_path)):
            os.makedirs(os.path.dirname(dest_path))

        with open(dest_path, 'wb') as f:
            f.write(file_bytes)
    
    def read_directory(
        self,
        dest_path: str,
        src_path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
    ) -> None:
        """
        Read directory folder contents specified by src_path or abspath and write them to dest_path.

        Attributes:
            dest_path: Absolute destination path to read the directory to. Positional only.
            src_path: Relative path to the source directory from within the IOReader's 
                      basepath directory. src_path ignored if abspath specified, so either 
                      specify src_path or abspath not both. Positional only.
            abspath: Absolute path to the source directory. If directory is on S3, use the format 
                     "s3://bucket/key". src_path ignored if abspath specified, so either specify 
                     src_path or abspath not both. Keyword only.
        """
        if not self.exists(src_path, abspath=abspath, is_folder=True):
            raise OSError("Source directory does not exist")

        if abspath is None:
            if src_path is None:
                raise ValueError("No src_path or abspath set.")
            # uses config to build full absolute path
            abspath = self.get_absolute_path(src_path)

        for file_abspath in self.list_directory(abspath=abspath):
            relative_path = os.path.relpath(file_abspath, abspath)
            self.read_file(os.path.join(dest_path, relative_path), abspath=file_abspath)

    def read_in_cache(
        self,
        cache_path: str,
    ) -> None:
        """
        If executing on the cloud, read in saved cloud cache if one exists and write it to cache_path. 
        If executing locally, it won't do anything.
    
        Attributes:
            cache_path: Absolute destination path to read the cache to.
        """
        if self.cloud_execution:
            try:                
                cache_name = f"{os.path.basename(cache_path)}.zip"
                cloud_path = self.get_absolute_path(cache_name, basepath=self.cloud_cache_basepath)

                if not self.exists(abspath=cloud_path):
                    if not os.path.exists(cache_path):
                        os.makedirs(cache_path)
                else:
                    self.read_zip_directory(cache_path, abspath=cloud_path)
            except botocore.exceptions.ClientError:
                if not os.path.exists(cache_path):
                    os.makedirs(cache_path)

    def read_zip_directory(
        self,
        dest_path: str,
        src_path: str | None = None,
        /, *, # before positional, after keyword
        abspath: str | None = None,
        format_archive: str="zip",
    ) -> None:
        """
        Read archived directory folder specified by src_path or abspath, unpack archived directory 
        (aka unzip it), and write it to dest_path.

        Attributes:
            dest_path: Absolute destination path to read the directory to. Positional only.
            src_path: Relative path to the source zipped directory/archive from within the IOReader's 
                      basepath directory. src_path ignored if abspath specified, so either specify 
                      src_path or abspath not both. Positional only.
            abspath: Absolute path to the source zipped directory/archive. If file is on S3, 
                     use the format "s3://bucket/key". src_path ignored if abspath specified, 
                     so either specify src_path or abspath not both. Keyword only.
            format_archive: Format of archived directory. Possible values are: "zip", "tar", 
                            "gztar", "bztar", and "xztar". By default, "zip". Keyword only.
        """
        # TODO: this code is repeated between read_zip_directory() and write_zip_directory(). 
        #       Let's reduce the repetition over time.
        if format_archive == "zip" or format_archive == "tar":
            ext = ext_regex = format_archive
            format_abbreviation = ""
        elif format_archive == "gztar":
            ext = "tar.gz"
            ext_regex = r"tar\.gz"
            format_abbreviation = 'gz'
        elif format_archive == "bztar":
            ext = "tar.bz2"
            ext_regex = r"tar\.bz2"
            format_abbreviation = 'bz2'
        elif format_archive == "xztar":
            ext = "tar.xz"
            ext_regex = r"tar\.xz"
            format_abbreviation = 'xz'
        else:
            format_archive = "zip"
            ext = ext_regex = format_archive
            format_abbreviation = ""

        if abspath is None:
            if src_path is None:
                raise ValueError("No src_path or abspath set.")
            # uses config to build full absolute path
            abspath = self.get_absolute_path(src_path)

        if not IOReader.check_extension(abspath, ext_regex):
            abspath = f"{abspath}.{ext}"

        if not self.exists(abspath=abspath):
            raise OSError("Source directory does not exist")

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        file_manager = self._get_file_manager(abspath=abspath)

        file_obj = file_manager.read_bytes()

        if format_archive == "zip":
            with zipfile.ZipFile(file_obj, mode="r") as archive:
                archive.extractall(dest_path)
        else:
            with tarfile.open(fileobj=file_obj, mode=f"r|{format_abbreviation}") as archive:
                if sys.version_info >= (3,12):
                    archive.extractall(dest_path, filter="data")
                else:
                    archive.extractall(dest_path)

        file_obj.close()
