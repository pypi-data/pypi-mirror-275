import io
import os
import gzip
import pickle
import tarfile
import zipfile
import pandas as pd

from .io_base import IOBase
from typing import Any
from .io_config import IOConfig


class IOWriter(IOBase):
    def __init__(
        self, 
        local_basepath: str | None = None,
    ) -> None:
        """
        Constructor for IOWriter. IOWriter allows you to write files to either the 
        output location (defined by CLOUD_WRITE_BASEPATH in .env) or the local_basepath, 
        depending on where your code is executing. By default, the local_basepath defined in 
        your .env file will be used but you can override that using the constructor argument.
    
        Attributes:
            local_basepath: basepath to use with writer when executing locally.
        
        """
        config = IOConfig()
        self.cloud_execution = config.cloud_execution
        if config.cloud_execution:
            self.basepath = config.cloud_write_basepath
            self.cloud_cache_basepath = config.cloud_cache_basepath
        else:
            self.basepath = local_basepath
            self.cloud_cache_basepath = None
            if self.basepath is None:
                self.basepath = config.local_write_basepath

    def write(
        self,
        body: str,
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        compress: bool = False,
    ) -> None:
        """
        Write body to file specified by path or abspath.
    
        Attributes:
            body: Contents to write to file. Positional only.
            path: Relative path within the IOWriter's basepath directory to write the file to, 
                  including file name and extension. path ignored if abspath specified, so either 
                  specify path or abspath not both. Positional only.
            abspath: Absolute path to write the file to, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored if abspath specified, 
                     so either specify path or abspath not both. Keyword only.
            compress: Whether to compress file using gzip. By default, False. Keyword only.
        """
        self.write_bytes(
            body.encode('utf-8'),
            path,
            abspath=abspath,
            compress=compress,
        )

    def write_bytes(
        self,
        body: bytes,
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        compress: bool = False,
    ) -> None:
        """
        Write byte string body to file specified by path or abspath.
    
        Attributes:
            body: Byte string contents to write to file. Positional only.
            path: Relative path within the IOWriter's basepath directory to write the file to, 
                  including file name and extension. path ignored if abspath specified, so either 
                  specify path or abspath not both. Positional only.
            abspath: Absolute path to write the file to, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored if abspath specified, 
                     so either specify path or abspath not both. Keyword only.
            compress: Whether to compress file using gzip. By default, False. Keyword only.
        """
        if abspath is None:
            if path is None:
                raise ValueError("No path or abspath set.")
            # uses config to build full absolute path
            abspath = self.get_absolute_path(path)

        if compress:
            if not IOWriter.check_extension(abspath, "gz"):
                abspath += ".gz"
            body = gzip.compress(body)

        file_manager = self._get_file_manager(abspath=abspath)

        file_obj = io.BytesIO(body)

        file_manager.write_bytes(file_obj)

        file_obj.close()

    def write_pickle(
        self,
        obj: Any,
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        compress: bool = False,
    ) -> None:
        """
        Pickle obj and write it to file specified by path or abspath.
    
        Attributes:
            obj: Object to write to file. Positional only.
            path: Relative path within the IOWriter's basepath directory to write the file to, 
                  including file name and extension. path ignored if abspath specified, so either 
                  specify path or abspath not both. Positional only.
            abspath: Absolute path to write the file to, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored if abspath specified, 
                     so either specify path or abspath not both. Keyword only.
            compress: Whether to compress file using gzip. By default, False. Keyword only.
        """
        body = pickle.dumps(obj)
        self.write_bytes(
            body,
            path,
            abspath=abspath,
            compress=compress,
        )
    
    def write_lines(
        self,
        lines: list[str],
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        compress: bool = False,
    ) -> None:
        """
        Write list of string lines to file specified by path.
    
        Attributes:
            lines: List of string lines to write to file. Positional only.
            path: Relative path within the IOWriter's basepath directory to write the file to, 
                  including file name and extension. path ignored if abspath specified, so either 
                  specify path or abspath not both. Positional only.
            abspath: Absolute path to write the file to, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored if abspath specified, 
                     so either specify path or abspath not both. Keyword only.
            compress: Whether to compress file using gzip. By default, False. Keyword only.
        """
        body = "\n".join(lines)
        self.write(
            body,
            path,
            abspath=abspath,
            compress=compress,
        )

    def write_df(
        self,
        df: pd.DataFrame,
        path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        compress: bool = False,
        filetype: str = "infer",
        pandas_args: dict | None = None
    ) -> None:
        """
        Write pandas Dataframe to file specified by path or abspath. File type automatically 
        determined from path/abspath. Note: only parquet, pickle, and csv files supported. 
        If another file type needed, please use write_bytes or write_file.
    
        Attributes:
            df: pandas Dataframe to write to file. Positional only.
            path: Relative path within the IOWriter's basepath directory to write the file to, 
                  including file name and extension. path ignored if abspath specified, so either 
                  specify path or abspath not both. Positional only.
            abspath: Absolute path to write the file to, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored if abspath specified, 
                     so either specify path or abspath not both. Keyword only.
            compress: Whether to compress file using gzip. By default, False. Keyword only.
            filetype: File type of file being written. Possible values are: "csv", "pickle", 
                      "parquet", and "infer". Defaults to "infer", which means type is inferred from the path. 
                      Keyword only.
            pandas_args: A dictionary of arguments to add when calling pandas function. Defaults to {}. Keyword only.
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

        if filetype == "pickle" or (
            filetype == "infer" and (
                IOWriter.check_extension(abspath, "pkl") or
                IOWriter.check_extension(abspath, r"pkl\.[a-zA-Z0-9]+")
            )
        ):
            if compress:
                if not IOWriter.check_extension(abspath, "gz"):
                    abspath += ".gz"
                pd_args["compression"] = "gzip"

            file_manager = self._get_file_manager(abspath=abspath)

            file_manager.write_df(df.to_pickle, pd_args)

        elif filetype == "parquet" or (
            filetype == "infer" and (
                IOWriter.check_extension(abspath, "parquet") or
                IOWriter.check_extension(abspath, r"parquet\.[a-zA-Z0-9]+") or
                IOWriter.check_extension(abspath, "pqt") or
                IOWriter.check_extension(abspath, r"pqt\.[a-zA-Z0-9]+")
            )
        ):
            if compress:
                if not IOWriter.check_extension(abspath, "gz"):
                    abspath += ".gz"
                pd_args["compression"] = "gzip"

            file_manager = self._get_file_manager(abspath=abspath)

            file_manager.write_df(df.to_parquet, pd_args)

        elif filetype == "csv" or (
            filetype == "infer" and (
                IOWriter.check_extension(abspath, "csv") or
                IOWriter.check_extension(abspath, r"csv\.[a-zA-Z0-9]+")
            )
        ):
            if "index" not in pd_args:
                pd_args["index"] = False
            body = df.to_csv(**pd_args)

            self.write(
                body,
                abspath=abspath,
                compress=compress,
            )
        else:
            raise ValueError(
                "Invalid df file type. only csv, pkl, and parquet supported. "
                "Try read file or read bytes."
            )

    def write_file(
        self,
        src_path: str,
        dest_path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        compress: bool = False, 
    ) -> None:
        """
        Write file from src_path to specified dest_path or abspath.
    
        Attributes:
            src_path: Absolute path to the source file, including file name and extension. 
                      Positional only.
            dest_path: Relative path within the IOWriter's basepath directory to write the file to, 
                       including file name and extension. path ignored if abspath specified, 
                       so either specify path or abspath not both. Positional only.
            abspath: Absolute path to write the file to, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". path ignored if abspath specified, 
                     so either specify path or abspath not both. Keyword only.
            compress: Whether to compress file using gzip. By default, False. Keyword only.
        """
        with open(src_path, "rb") as f:
            body = f.read()

        self.write_bytes(
            body,
            dest_path,
            abspath=abspath,
            compress=compress,
        )

    def write_directory(
        self,
        src_path: str,
        dest_path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
    ) -> None:
        """
        Write directory folder contents from src_path to specified dest_path or abspath.
    
        Attributes:
            src_path: Absolute path to the source directory. Positional only.
            dest_path: Relative path within the IOWriter's basepath directory to write the directory to. 
                       dest_path ignored if abspath specified, so either specify dest_path or abspath 
                       not both. Positional only.
            abspath: Absolute path to write the directory to. If directory is on S3, 
                     use the format "s3://bucket/key". dest_path ignored if abspath specified, 
                     so either specify dest_path or abspath not both. Keyword only.
        """
        if not self.exists(abspath=src_path, is_folder=True):
            raise OSError("Source directory does not exist")

        if abspath is None:
            if dest_path is None:
                raise ValueError("No dest_path or abspath set.")
            # uses config to build full absolute path
            abspath = self.get_absolute_path(dest_path)

        for file_abspath in self.list_directory(abspath=src_path):
            relative_path = os.path.relpath(file_abspath, src_path)

            full_dest_path = os.path.join(abspath, relative_path)
            
            self.write_file(file_abspath, abspath=full_dest_path)
    
    def write_out_cache(
        self,
        cache_path: str,
    ) -> None:
        """
        If executing on the cloud, archive (aka zip) directory folder specified by cache_path
        and save it to cloud_cache_basepath on S3. If executing locally, it won't do anything.
        
        Attributes:
            cache_path: Absolute destination path to write the cache to.
        """
        if self.cloud_execution:
            if not os.path.exists(cache_path):
                os.makedirs(cache_path)

            cache_name = os.path.basename(cache_path)

            cloud_path = self.get_absolute_path(cache_name, basepath=self.cloud_cache_basepath)

            self.write_zip_directory(cache_path, abspath=cloud_path)

    def write_zip_directory(
        self,
        src_path: str,
        dest_path: str | None = None, 
        /, *, # before positional, after keyword
        abspath: str | None = None,
        format_archive: str="zip",
    ) -> None:
        """
        Archive (aka zip) and write directory folder specified at src_path to the dest_path or abspath.

        Attributes:
            src_path: Absolute path to the source directory to zip. Positional only.
            dest_path: Relative path within the IOWriter's basepath directory to write the 
                       zipped directory to, including file name and extension. dest_path ignored 
                       if abspath specified, so either specify dest_path or abspath not both. 
                       Positional only.
            abspath: Absolute path to write the zipped directory to, including file name and extension. 
                     If file is on S3, use the format "s3://bucket/key". dest_path ignored if abspath 
                     specified, so either specify dest_path or abspath not both. Keyword only.
            format_archive: Format of archived directory. Possible values are: "zip", "tar", "gztar", 
                            "bztar", and "xztar". By default, "zip".
        """
        if not self.exists(abspath=src_path, is_folder=True):
            raise OSError("Source directory does not exist")

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
            if dest_path is None:
                raise ValueError("No dest_path or abspath set.")
            # uses config to build full absolute path
            abspath = self.get_absolute_path(dest_path)

        if not IOWriter.check_extension(abspath, ext_regex):
            abspath = f"{abspath}.{ext}"

        file_obj = io.BytesIO()

        if format_archive == "zip":
            with zipfile.ZipFile(file_obj, 'w', zipfile.ZIP_DEFLATED) as archive:
                # add directory (needed for empty dirs)
                archive.write(".")
                for file_abspath in self.list_directory(abspath=src_path):
                    relative_path = os.path.relpath(file_abspath, src_path)

                    archive.write(file_abspath, arcname=relative_path)
        else:
            with tarfile.open(fileobj=file_obj, mode=f"w|{format_abbreviation}") as archive:
                archive.add(src_path, arcname=".")

        file_manager = self._get_file_manager(abspath=abspath)

        file_manager.write_bytes(file_obj)

        file_obj.close()
