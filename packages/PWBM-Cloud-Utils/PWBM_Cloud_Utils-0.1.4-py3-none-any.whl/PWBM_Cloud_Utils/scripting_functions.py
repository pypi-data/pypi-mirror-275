from .api_functions import ModelsAPI, ScenarioAPI, ScenarioUploadData
from typing_extensions import Self
from typing import Any
import dataclasses
from .cloud_main import CloudMain
import os
import pandas as pd
import json
import glob
import tempfile
import zipfile
import io


class FilePath:
    _file_path: str

    def __init__(self, file_path: str):
        self._file_path = file_path

    def read(self) -> Any:
        """
        Read out the data from the file path. Currently we only support csv and json files.

        Returns:
            Dataframe if it is a csv file,
            string/dict/list if it is a json file, depending on the contents in it,
            and raise exception if neither
        """
        if self._file_path.endswith(".csv"):
            return pd.read_csv(self._file_path)
        elif self._file_path.endswith(".json"):
            with open(self._file_path, 'r') as json_file:
                return json.load(json_file)
        else:
            raise Exception("Unsupported file type.")


class Model:
    # This private information is used by run(), but general users should not access this.
    _id: int
    _models_api: ModelsAPI

    def __init__(
        self,
        id: int,
        models_api: ModelsAPI | None = None
    ):
        self._id = id
        if models_api is None:
            self._models_api = ModelsAPI()
        else:
            self._models_api = models_api

    @staticmethod
    def load(model_id: int, models_api: ModelsAPI | None = None) -> Self:
        """
        Load a model from database based on model id
        Attributes:
            model_id: id of the model
            models_api: the api used to get model

        Returns:
            Model object
        """
        if models_api is None:
            models_api = ModelsAPI()
        response = models_api.get_model(model_id)

        return Model(response['id'], models_api)

    # @staticmethod
    # def create(name: str, description: str, git_repo: str, git_branch: str, models_api: ModelsAPI | None = None) -> Self:
    #     data = {
    #         "name": name,
    #         "description": description,
    #         "git_repo": git_repo,
    #         "git_branch": git_branch
    #     }
    #     response = models_api.create_model(data)
    #     return Model(
    #         response['id'],
    #         models_api
    #     )


class Scenario:
    # None indicates that the data is not available in the cloud. See .is_on_cloud().
    _scenario_id: int | None
    _model_id: int
    _object_path: tempfile.TemporaryDirectory
    _scenario_api: ScenarioAPI

    def __init__(
        self,
        scenario_id: int | None,  # None indicates that it is unknown
        model_id: int,
        object_path: tempfile.TemporaryDirectory,
        scenario_api: ScenarioAPI | None = None
    ):
        """
        scenario_id: id of the scenario in S3, None indicates that it is a local scenario with unknown id
        model_id: id of the model associated with the scenario
        object_path: temporary directory to store the config path. This location 
                     is cleaned up by Scenario when the object is deleted. 
        scenario_api: ScenarioApi to load, push and execute a scenario
        """
        self._scenario_id = scenario_id
        self._model_id = model_id

        if not os.path.isdir(object_path.name):
            raise ValueError(
                 "object_path should be a valid directory with files containing "
                 "information about the Scenario objects.")
        self._object_path = object_path

        if scenario_api is None:
            self._scenario_api = ScenarioAPI()
        else:
            self._scenario_api = scenario_api

    def _push(self) -> None:
        """
        Pushes the Scenario to the cloud. It should be called implicitly in the run method, and not accessed by the user.  
        If you want to create a Scenario locally, e.g. 
        Scenario.new() or Scenario.clone(), and not register it with the API, don't call 
        this method.
        """
        # TODO: we might need a better way to detect changes by comparing the config files
        # to avoid the case like users change values after __getitem__
        if self._scenario_id is None:
            # zip a folder
            # TODO: what file name should we pass
            # Currently we expect user to provide objects = {"runtime_options": xxx} for new method,
            # but if they can provide objects = {"agi_surtax/runtime_options": xxx} where every key start with "agi_surtax/", we probably can extract
            # the scenario name from the key and get rid of zip_file_name in zipf.write(file_path, os.path.join(zip_file_name, arcname))
            zip_file_name = f"scenario_config"

            # Create an in-memory buffer to store the zip file
            zip_buffer = io.BytesIO()

            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(self._object_path.name):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self._object_path.name)
                        zipf.write(file_path, os.path.join(zip_file_name, arcname))

            # Seek to the beginning of the buffer
            zip_buffer.seek(0)

            # Read the contents of the zip file from the buffer
            zip_content = zip_buffer.read()

            # Create a scenario on cloud
            data = ScenarioUploadData(
                model_id=self._model_id,
                folder_name=f"{zip_file_name}.zip",
                file=zip_content,
            )
            scenario_data = self._scenario_api.create_scenario(data)

            # Set the private attribute to indicate that it is on cloud
            self._scenario_id = scenario_data["id"]

    @staticmethod
    def new(
        model: Model, objects: dict[str, Any], scenario_api: ScenarioAPI | None = None,
    ) -> Self:
        """
        Create a new scenario object locally and associate it with an existing model
        Attributes:
            model: the model object of the scenario
            objects: a dictionary contains parameters and values for the scenario. We accept values as pd.DataFrame, string, list or dictionary.

        Returns: 
            Scenario object
        """
        # Create the temp directory and get the name
        object_path = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)

        # Iterate over the provided objects
        for param_name, param_data in objects.items():
            if isinstance(param_data, FilePath):
                param_data = param_data.read()

            file_name_without_extension = os.path.basename(param_name)
            dir_path = os.path.join(object_path.name, os.path.dirname(param_name))

            ## Check existence of directory and create it if not
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            if isinstance(param_data, (dict, str, list)):
                # Write to json file
                with open(os.path.join(dir_path, f"{file_name_without_extension}.json"), 'w') as json_file:
                    json.dump(param_data, json_file)

            elif isinstance(param_data, pd.DataFrame):
                ## Write to csv file
                # TODO: not sure whether index should be set to False or True as currently we don't have scenario files which are csv files
                param_data.to_csv(os.path.join(dir_path, f"{file_name_without_extension}.csv"), index=False)

        return Scenario(None, model._id, object_path, scenario_api)

    @staticmethod
    def load(scenario_id: int, scenario_api: ScenarioAPI | None = None) -> Self:
        """
        Fetch an existing scenario from DB, and the config files go to an unspecified temp folder

        Attributes:
            scenario_id: the id of the scenario to fetch from the database
            scenarios_api: scenario_api: ScenarioApI to load, push and execute a scenario

        Returns:
            Scenario object
        """
        if scenario_api is None:
            scenario_api = ScenarioAPI()

        # get scenario data
        response = scenario_api.get_scenario_by_id(scenario_id)

        scenario_data = dataclasses.asdict(response)

        # Create the temp directory and get the name to hold config files
        object_path = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        # download config file
        CloudMain(scenario_id, object_path.name)

        return Scenario(scenario_id, scenario_data["model_id"], object_path, scenario_api)

    def __del__(self):
        """
        This is called with object is cleared from memory.
        """
        self._object_path.cleanup()

    def __getitem__(self, key):
        """
        This is to get values for parameters in config files
        """
        path = os.path.join(self._object_path.name, os.path.normpath(key))
        files = glob.glob(path + '.*')  # TODO: we want to limit this to just csv and json
        if not files:
            raise ValueError(f"There is no configuration corresponding to {key}.")

        data = Scenario._read_file_data(files[0])  # TODO: this is not a great idea to use files[0]

        return data

    def __setitem__(self, key, value):
        """
        This is to set values for parameters in config files
        """
        if isinstance(value, FilePath):
            value = value.read()

        path = os.path.join(self._object_path.name, os.path.normpath(key))
        files = glob.glob(path + '.*')  # TODO: we want to limit this to just csv and json
        if not files:
            raise ValueError(f"There is no configuration corresponding to {key}.")

        root = os.path.splitext(files[0])[0] # TODO: this is not a great idea to use files[0]
        # TODO: what if user wants to write a dataframe to a json file
        if isinstance(value, (dict, list, str)):
            # If data is a dictionary, store it as a JSON file
            with open(f"{root}.json", 'w') as json_file:
                json.dump(value, json_file)

        elif isinstance(value, pd.DataFrame):
            # If data is a DataFrame, store it as a CSV file
            value.to_csv(f"{root}.csv", index=False)

        # Invalidate the scenario ID if anything is modified.
        self._scenario_id = None

    def _read_directory_data(self) -> dict[str, Any]:
        """
        Read data from the object path

        Returns:
            a dictionary contains parameter names and parameter values read out from scenario object path, where the config file locates
        """
        directory_data = {}

        # Iterate over all files and subdirectories in the directory and add to directory data
        for root, dirs, files in os.walk(self._object_path.name):
            for file_name in files:
                # Get full file path and read data
                file_path = os.path.join(root, file_name)
                data = Scenario._read_file_data(file_path)

                # get relative path relative to the temp folder path
                relative_path = os.path.relpath(file_path, self._object_path.name)

                # remove file extension from file path
                rel_path_without_extension = os.path.splitext(relative_path)[0]

                # change path to key of "dir/subdir/filename" format
                param_key = os.path.normpath(rel_path_without_extension).replace("\\", "/")
                
                directory_data[param_key] = data

        return directory_data

    @staticmethod
    def _read_file_data(file_path: str) -> Any:
        """
        Read out data from a given csv/json file path

        Attributes:
            file_path: absolute file path

        Returns:
            a dataframe if reading from a csv file, or 
        """
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension == '.csv':
                # Read CSV file as dataframe
                dataframe = pd.read_csv(file_path)
                return dataframe
            elif file_extension == '.json':
                # Read JSON file as dictionary
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    return data
            else:
                raise ValueError("Unsupported file type!")
        else:
            raise ValueError("File path not valid!")

    def clone(self, *, objects_to_override: dict[str, Any] | None = None) -> Self:
        """
        Create counterfactuals from baseline or implement stacking.
        """
        source_object = self._read_directory_data()

        # Override certain key value pairs:
        if objects_to_override is not None:
            for key, val in objects_to_override.items():
                source_object[key] = val

        # Create the cloned scenario
        cloned_scenario = Scenario.new(Model.load(self.model_id), source_object, self._scenario_api)

        return cloned_scenario

    @property
    def model_id(self) -> int:
        return self._model_id

    def is_on_cloud(self) -> bool:
        """
        Check whether the scenario is on cloud

        Returns:
            True if the scenario is on cloud and False if it exists locally
        """
        return self._scenario_id is not None


def run(
    model: Model,
    scenarios: list[Scenario],
    *,
    local_execution: bool = False,
    # TODO: it is a little strange that scenario_api is needed in addition to a scenario.
    scenario_api: ScenarioAPI | None = None,
) -> None:
    """
    Currently run only supports cloud execution.
    Note that Scenario.push() is called on all Scenario objects since the Model
    downloads the Sencarios from the API.

    Future:
    local_execution=True can be used to pull the container down and run it
    locally while using the data in the cloud. This can be a good way to debug
    issues before running it fully on the cloud.

    QUESTION: can we create an image where the code comes from the local file
    system? This can really help people debug, especially coupled with VSCode
    Dev Container extension.
    """
    if scenario_api is None:
        scenario_api = ScenarioAPI()

    # Check model id and scenarios' model id are consistent
    for scenario in scenarios:
        if scenario.model_id != model._id:
            raise ValueError("Scenario's model ID and model's ID don't match.")

    # Support cloud execution of list of scenarios
    if not local_execution:
        for scenario in scenarios:
            # Push scenarios to S3 if it is a local scenario
            if not scenario.is_on_cloud():
                scenario._push()
            scenario_api.execute_scenario(scenario._scenario_id)
