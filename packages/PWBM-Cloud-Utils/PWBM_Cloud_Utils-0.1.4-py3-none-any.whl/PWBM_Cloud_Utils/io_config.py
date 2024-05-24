from dotenv import load_dotenv
import os
import re


class IOConfig:
    cloud_read_basepath: str | None
    cloud_write_basepath: str | None
    local_read_basepath: str | None
    local_write_basepath: str | None
    cloud_cache_basepath: str | None
    cloud_execution: bool

    def __init__(self):
        """
        Constructor for IOConfig. IOConfig uses the local .env file to set config 
        settings. Some settings are overridable with the constructor.
        """
        load_dotenv(".env")

        # TODO: also edit yaml in WITS_API (was CloudData)
        cloud_exec_key = "CLOUD_EXECUTION"
        if cloud_exec_key in os.environ:
            if os.environ[cloud_exec_key].upper() == "TRUE":
                self.cloud_execution = True
            elif os.environ[cloud_exec_key].upper() == "FALSE":
                self.cloud_execution = False
            else:
                raise AssertionError(
                    f'Environment Variable {cloud_exec_key} value of '
                    f'"{os.environ[cloud_exec_key]}" is not a proper boolean.  Use "True" or "False".'
                )
        else:
            self.cloud_execution = False
       
        # TODO: also edit yaml in WITS_API (was aws_model_bucket)
        if "CLOUD_READ_BASEPATH" in os.environ:
            self.cloud_read_basepath = os.environ["CLOUD_READ_BASEPATH"]
        else:
            self.cloud_read_basepath = None

        if "CLOUD_WRITE_BASEPATH" in os.environ:
            self.cloud_write_basepath = os.environ["CLOUD_WRITE_BASEPATH"]
        else:
            self.cloud_write_basepath = None

        if "LOCAL_READ_BASEPATH" in os.environ:
            self.local_read_basepath = os.environ["LOCAL_READ_BASEPATH"]
        else:
            self.local_read_basepath = None

        if "LOCAL_WRITE_BASEPATH" in os.environ:
            self.local_write_basepath = os.environ["LOCAL_WRITE_BASEPATH"]
        else:
            self.local_write_basepath = None

        if "CLOUD_CACHE_BASEPATH" in os.environ:
            self.cloud_cache_basepath = os.environ["CLOUD_CACHE_BASEPATH"]
        else:
            self.cloud_cache_basepath = None
