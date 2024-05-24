import os


def compare_path(path_1: str, path_2: str) -> bool:
    """
    Compares if paths are the same, regardless of separator used. 
    Different OS/platform may use different separators, e.g. Windows uses \ whereas
    S3 or Linux uses /. FileManager.normpath() normalizes the returned path depending
    on OS/platform, which is why this is necessary.
    """
    return os.path.relpath(path_1, path_2) == '.'
