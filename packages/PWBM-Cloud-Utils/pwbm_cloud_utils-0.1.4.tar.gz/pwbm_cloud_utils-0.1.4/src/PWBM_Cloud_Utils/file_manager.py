from collections import namedtuple
# typing_extensions can be removed on Python 3.10+:
from typing import Any, ClassVar
from typing_extensions import Self, BinaryIO, Iterator, Callable, NamedTuple
import re
import os
import boto3
import botocore
import io
from abc import ABC, abstractmethod


class FileManager(ABC):
    """
    File managers take in the absolute path to some file or directory and provide 
    methods for interacting with that file or directory.

    Currently, a new File Manager should be created for each abspath rather than
    creating a single manager when instantiating the reader or writer and then using
    that manager for all subsequent reads/writes. The reason for this is that instantiating
    a file manager is currently low cost, partially because we are only connecting
    to S3 once when the first S3 file manager is created. If we encounter file managers
    that are costly to instantiate, we may want to move to creating one default
    manager per reader/writer.
    """
    abspath: str

    def __init__(self, abspath: str):
        """
        Base constructor for a file manager

        Attributes:
            abspath : an absolute path to the file/folder, including file name and extension.

        """
        self.abspath = self.normpath(abspath)

    @staticmethod
    def is_s3_path(abspath: str) -> bool:
        """
        Determine if given path is an S3 absolute path path ("s3://bucket/...").

        Attributes:
            abspath : absolute path to the file/folder, including file name and extension.

        Returns: whether or not it is a S3 absolute path.
        """
        # Bucket names can consist only of lowercase letters, numbers, dots (.), and hyphens (-).
        # todo, what if bucket only and no final slash
        p = re.compile(r'^[sS]3:\/\/(?P<bucket>(\d|[a-z]|-|\.)+)\/(?P<path>.*)$')

        return p.match(abspath)

    @staticmethod
    def new(abspath: str) -> Self:
        """
        Static factory constructor for file managers. This determines the correct 
        file manager to return based on the given absolute path.

        Attributes:
            abspath : absolute path to the file/folder, including file name and extension.

        Returns: a concrete file manager that works with that absolute path
        """
        if FileManager.is_s3_path(abspath):
            return S3FileManager(abspath)
        else:
            return LocalFileManager(abspath)

    @abstractmethod
    def read_bytes(self) -> BinaryIO:
        """
        Reads the file specified by the file manager's abspath and returns a file-like
        bytes object with the pointer set at beginning of file.

        Returns: a file-like bytes object with the pointer set at beginning of file.
        """
        pass

    @abstractmethod
    def write_bytes(self, body: BinaryIO) -> None:
        """
        Takes a file-like bytes object and writes it to the file manager's abspath.
        
        Note: the pointer will be set at beginning of file.
        Note: will make the path to the file if it does not already exist.

        Attributes:
            body : a file-like bytes object

        """
        pass

    @abstractmethod
    def list_directory(self, regex_search: str = "") -> Iterator[str]:
        """
        List contents of directory specified by the file manager's abspath with an Iterator.

        Note: This method lists only the files in the directory, so empty subdirectories not included.
        Note: all files in the directory will be included, including those in any subdirectory.
        Note: the string for each file is the absolute path to that file. 

        Attributes:
            regex_search: only results that match regex pattern will be included.

        Returns: string iterator of directory contents
        """
        pass

    @abstractmethod
    def exists(self, is_folder: bool=False) -> bool:
        """
        Determines if the file or folder specified by the file manager's abspath exists.

        Note: is_folder is needed because the method for checking existence on S3 is 
        different for files than for folders and we do not have a consistent way to 
        tell from the path if it is a folder or a path. We can get rid of it if a method 
        is provided by S3 that works on either folders or files or if we have a way 
        to consistently identify folders.

        Attributes:
            is_folder: Whether the given path is to a folder.

        Returns: whether the file or folder specified by the file manager's abspath exists.
        """
        pass

    @staticmethod
    def normpath(path) -> str:
        """
        Normalize path based on the file manager specifications.

        Attributes:
            path: path to normalize. can be a relative path or absolute.

        Returns: normalized path
        """
        return os.path.normpath(path)

    def read_df_target(self) -> str | io.BytesIO:
        """
        Get target to be used with a pd.read function based on file manager's abspath.

        Note: Most pandas read functions can accept a string target or a file-like bytes object target.
              If pandas has their own implementation of accessing the file, it is typically more reliable
              to use their implementation, but otherwise using a io.BytesIO should work most of the time.

        Returns: a target to be used with a pd.read function based on file manager's abspath
        """
        response = self.read_bytes()

        return io.BytesIO(response)
    
    def write_df(self, pandas_method: Callable[..., None], pandas_args: dict | None = None) -> None:
        """
        Use given pandas_method (should be a df.to_... method) from the df you want to write
        and write output to location specified by file manager's abspath.

        Attributes:
            pandas_method: A pandas write method from relevent df (ie df.to_csv or df.to_parquet)
            pandas_args: A dictionary of arguments to add when calling pandas method.

        """
        if pandas_args is None:
            pandas_args = {}

        file_obj = io.BytesIO()

        pandas_method(file_obj, **pandas_args)

        self.write_bytes(file_obj.getvalue())



class LocalFileManager(FileManager):
    """
    File manager for interacting with files mapped to the local file system,
    including network drives.
    """

    def read_bytes(self) -> BinaryIO:
        """
        Reads the file specified by the file manager's abspath and returns a file-like
        bytes object with the pointer set at beginning of file.

        Returns: a file-like bytes object with the pointer set at beginning of file.
        """
        return open(self.abspath, "rb")
    
    def write_bytes(self, body: BinaryIO) -> None:
        """
        Takes a file-like bytes object and writes it to the file manager's abspath.

        Note: the pointer will be set at beginning of file.
        Note: will make the path to the file if it does not already exist.

        Attributes:
            body : a file-like bytes object

        """
        if not os.path.exists(os.path.dirname(self.abspath)):
            os.makedirs(os.path.dirname(self.abspath))

        # move to beginning of stream in case not currently pointing there.
        body.seek(0)

        with open(self.abspath, 'wb') as f:
            f.write(body.read())

    def list_directory(self, regex_search: str = "") -> Iterator[str]:
        """
        List contents of directory specified by the file manager's abspath with an Iterator.

        Note: This method lists only the files in the directory, so empty subdirectories not included.
        Note: all files in the directory will be included, including those in any subdirectory.
        Note: the string for each file is the absolute path to that file. 

        Attributes:
            regex_search: only results that match regex pattern will be included.

        Returns: string iterator of directory contents
        """
        for dirpath, _, filenames in os.walk(self.abspath):  
            for filename in filenames:

                curr_path = os.path.join(dirpath, filename)
                
                if re.search(regex_search, curr_path):
                    yield self.normpath(curr_path)
    
    def exists(self, is_folder: bool = False) -> bool:
        """
        Determines if the file or folder specified by the file manager's abspath exists.

        Note: need named is_folder even if not used because used as a key word arg

        Attributes:
            is_folder: Whether the given path is to a folder.

        Returns: whether the file or folder specified by the file manager's abspath exists.
        """
        return os.path.exists(self.abspath)
    
    def read_df_target(self) -> str | io.BytesIO:
        """
        Get target to be used with a pd.read function based on file manager's abspath.

        Note: pandas can handle local files itself, so passing target as a string.

        Returns: a target to be used with a pd.read function based on file manager's abspath
        """
        return self.abspath
    
    def write_df(self, pandas_method: Callable[..., None], pandas_args: dict | None = None) -> None:
        """
        Use given pandas_method (should be a df.to_... method) from the df you want to write
        and write output to location specified by file manager's abspath.

        Attributes:
            pandas_method: A pandas write method from relevent df (ie df.to_csv or df.to_parquet)
            pandas_args: A dictionary of arguments to add when calling pandas method.

        """
        if pandas_args is None:
            pandas_args = {}

        if not os.path.exists(os.path.dirname(self.abspath)):
            os.makedirs(os.path.dirname(self.abspath))

        pandas_method(self.abspath, **pandas_args)


class S3Path(NamedTuple):
    """
    Helper class for parsing info from an S3 absolute path
    """
    bucket: str
    path: str

class S3FileManager(FileManager):
    """
    File manager for interacting with files inside an S3 bucket on AWS.
    """
    # boto3 does not support type annotation yet. See 
    #     https://github.com/boto/boto3/issues/1055#issuecomment-1380848223
    __resource: ClassVar[Any]=None
    __client: ClassVar[Any]=None

    bucket_name: str
    path: str

    def __init__(self, abspath: str):
        """
        Constructor for an S3 file manager

        Attributes:
            abspath : an absolute path to the file/folder, including file name and extension.

        """
        super().__init__(abspath)

        path_tuple = S3FileManager.parse_s3_path(self.abspath)

        if path_tuple.bucket == "" and path_tuple.path == "":
            raise ValueError("abspath is not a valid s3 path.")

        # data on S3
        self.bucket_name = path_tuple.bucket
        self.path = path_tuple.path


    @property
    def resource(self):
        """
        Some lazy loading since establishing a connection can be expensive. 
        """
        if S3FileManager.__resource is None:
            S3FileManager.__resource = boto3.resource("s3")
        
        return S3FileManager.__resource

    @property
    def client(self):
        """
        Some lazy loading since establishing a connection can be expensive. 
        """
        if S3FileManager.__client is None:
            S3FileManager.__client = boto3.client("s3")

        return S3FileManager.__client

    @staticmethod
    def parse_s3_path(s3_path: str) -> S3Path:
        """
        Read given S3 URI path into a tuple with bucket name and path. Returns None 
        if path does not match S3 URI format.
    
        Attributes:
            s3_path : S3 URI path to the file/folder, including file name and extension.
        
        Returns: bucket name and path are returned using S3Path. An empty S3Path is
                 returned if parsing fails.
        """
        # Bucket names can consist only of lowercase letters, numbers, dots (.), and hyphens (-).
        p = re.compile(r'^[sS]3:\/\/(?P<bucket>(\d|[a-z]|-|\.)+)\/(?P<path>.*)$')

        m = p.match(s3_path)
        if m:
            return S3Path(m.group('bucket'), m.group('path'))
        else:
            return S3Path("", "")

    def read_bytes(self) -> BinaryIO:
        """
        Reads the file specified by the file manager's abspath and returns a file-like
        bytes object with the pointer set at beginning of file.

        Returns: a file-like bytes object with the pointer set at beginning of file.
        """
        response_body = io.BytesIO()
        self.resource.Object(self.bucket_name, self.path).download_fileobj(response_body)

        # download_fileobj moves the pointer to the end of stream so reset to start
        response_body.seek(0)

        return response_body
    
    def write_bytes(self, body: BinaryIO) -> None:
        """
        Takes a file-like bytes object and writes it to the file manager's abspath.
        
        Note: the pointer will be set at beginning of file.
        Note: will make the path to the file if it does not already exist.

        Attributes:
            body : a file-like bytes object

        """
        # move to beginning of stream in case not currently pointing there.
        body.seek(0)
        self.resource.Object(self.bucket_name, self.path).upload_fileobj(body)

    def list_directory(self, regex_search: str = "") -> Iterator[str]:
        """
        List contents of directory specified by the file manager's abspath with an Iterator.

        Note: This method lists only the files in the directory, so empty subdirectories not included.
        Note: all files in the directory will be included, including those in any subdirectory.
        Note: the string for each file is the absolute path to that file. 

        Attributes:
            regex_search: only results that match regex pattern will be included.

        Returns: string iterator of directory contents
        """
        # filter by path and substring
        paginator = self.client.get_paginator('list_objects_v2')

        path = self.path

        if path == "." or path == "":
            pages = paginator.paginate(Bucket=self.bucket_name)
        else:
            # if path doesn't end in slash add one
            if path[-1] != "/":
                path = f"{path}/"
            pages = paginator.paginate(Bucket=self.bucket_name, Prefix=path)

        for page in pages:
            for obj in page['Contents']:
                key = obj['Key']
                # filter by path and search_regex and filter out the folders so only files in list
                if re.search(regex_search, key) and not re.search('^.+/$', key):
                    yield f"s3://{self.bucket_name}/{key}"
    
    def exists(self, is_folder: bool=False) -> bool:
        """
        Determines if the file or folder specified by the file manager's abspath exists.

        Note: is_folder is needed because the method for checking existence on S3 is 
        different for files than for folders and we do not have a consistent way to 
        tell from the path if it is a folder or a path. We can get rid of it if a method 
        is provided by S3 that works on either folders or files or if we have a way 
        to consistently identify folders.

        Attributes:
            is_folder: Whether the given path is to a folder.

        Returns: whether the file or folder specified by the file manager's abspath exists.
        """
        path = self.path

        if path[-1] == "/":
            is_folder = True
            path = path[:-1]

        try:
            if is_folder:
                if path == "." or path == "":
                    self.client.head_bucket(Bucket=self.bucket_name)
                    return True
                else:
                    response = self.client.list_objects(Bucket=self.bucket_name, Prefix=path, Delimiter='/',MaxKeys=2)
                    return 'CommonPrefixes' in response
            else:
                self.resource.Object(self.bucket_name, path).content_type
        except botocore.exceptions.ClientError:
            return False
        return True

    @staticmethod
    def normpath(path) -> str:
        """
        Normalize path based on the file manager specifications.

        Note: S3 needs "/" separators

        Attributes:
            path: path to normalize. can be a relative path or absolute.

        Returns: normalized path
        """
        # TODO: should we call something like os.path.normpath() to simplify the path?
        return path.replace("\\", "/")

    def read_df_target(self) -> str | io.BytesIO:
        """
        Get target to be used with a pd.read function based on file manager's abspath.

        Note: pandas can handle S3 files itself, so passing target as a string.

        Returns: a target to be used with a pd.read function based on file manager's abspath
        """
        return self.abspath
    
    def write_df(self, pandas_method: Callable[..., None], pandas_args: dict | None = None) -> None:
        """
        Use given pandas_method (should be a df.to_... method) from the df you want to write
        and write output to location specified by file manager's abspath.

        Attributes:
            pandas_method: A pandas write method from relevent df (ie df.to_csv or df.to_parquet)
            pandas_args: A dictionary of arguments to add when calling pandas method.

        """
        if pandas_args is None:
            pandas_args = {}
        pandas_method(self.abspath, **pandas_args)
