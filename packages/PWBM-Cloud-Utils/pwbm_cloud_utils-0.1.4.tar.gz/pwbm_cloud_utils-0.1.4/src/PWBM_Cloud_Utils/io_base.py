import os
import re
from .file_manager import FileManager


class IOBase:
    """
    IOBase acts as the base for IOReader and IOWriter and provides a few methods used by both.
    """
    basepath: str

    def __init__(
        self,
        basepath: str,
    ) -> None:
        """
        Constructor for IOBase. IOBase acts as the base for IOReader and IOWriter. 
        The inits for IOReader and IOWriter set self.basepath.

        Attributes:
            basepath: basepath to use

        """
        self.basepath = basepath

    def _get_file_manager(
        self,
        path: str | None = None, 
        /, *,  # before positional, after keyword
        abspath: str | None = None,
    ) -> FileManager:
        """
        """
        if abspath is None:
            if path is None:
                raise ValueError("No path or abspath set.")
            # uses config to build full absolute path
            abspath = self.get_absolute_path(path)

        return FileManager.new(abspath)

    @staticmethod
    def check_extension(path: str, ext_regex: str) -> bool:
        """
        Helper for checking if the path has the given extension

        Attributes:
            path: either an absolute path or a relative path to a file
            ext: extension you are looking for. should not include leading "." (ie "csv" or "pkl.gz")

        Returns:
            bool: True if the path has the extension
        """
        if not re.search(r'^\\\..*', ext_regex):
            ext_regex = f"\\.{ext_regex}"
        return re.search(f'.+{ext_regex}$', path) is not None

    def get_absolute_path(
        self, path: str,
        /, *,  # before positional, after keyword
        basepath: str | None = None,
    ) -> str:
        """
        Gets absolute path by joining the given path to either the IOReader's basepath 
        by default or the given basepath if specified. See IOReader constructor 
        for more info about the basepath.

        Attributes:
            path: relative path to a file or a folder. To reference the root of the basepath, 
                  either "." or "" accepted.
            basepath: Optional basepath to override IOReader's basepath. Defaults to None.

        Returns:
            str: absolute path from joining path to basepath.
        """
        if basepath is None:
            if self.basepath is None:
                raise ValueError("No basepath set.")
            basepath = self.basepath

        # TODO: it would be very convenient to call FileManager.normpath() for this.
        #       Should we move this method to FileManager?
        if path not in ("", "."):
            return os.path.join(basepath, path)

        else:
            return basepath

    def list_directory(
        self,
        path: str | None = None, 
        /, *,  # before positional, after keyword
        abspath: str | None = None,
        regex_search: str = "",
    ) -> list[str]:
        """
        List all files in directory at specified location, including those in subfolders. 
        Note that only files included in returned list.

        Attributes:
            path: Relative path to the directory from within the IOReader's basepath directory. path 
                  ignored if abspath specified, so either specify path or abspath not both. Positional only.
            abspath: Absolute path to the directory. If file is on S3, use the format "s3://bucket/key". 
                     path ignored if abspath specified, so either specify path or abspath not both. Keyword only.
            regex_search: only results that match regex pattern will be included. Keyword only.

        Returns: list of files located in the directory and all subdirectories. 
        """
        if not self.exists(path, abspath=abspath, is_folder=True):

            raise OSError("Directory does not exist")

        file_manager = self._get_file_manager(path, abspath=abspath)

        return list(file_manager.list_directory(regex_search=regex_search))

    def exists(
        self, 
        path: str | None = None, 
        /, *,  # before positional, after keyword
        abspath: str | None = None,
        is_folder: bool = False,
    ) -> bool:
        """
        Check if file or directory specified by path exists.

        Attributes:
            path: Relative path to the directory from within the IOReader's basepath directory. path 
                  ignored if abspath specified, so either specify path or abspath not both. Positional only.
            abspath: Absolute path to the directory. If file is on S3, use the format "s3://bucket/key". 
                     path ignored if abspath specified, so either specify path or abspath not both. Keyword only.
            is_folder: Whether the given path is to a folder. Keyword only.

        Returns:
            bool: True if file or directory exists, otherwise False.
        """
        file_manager = self._get_file_manager(path, abspath=abspath)

        return file_manager.exists(is_folder)
