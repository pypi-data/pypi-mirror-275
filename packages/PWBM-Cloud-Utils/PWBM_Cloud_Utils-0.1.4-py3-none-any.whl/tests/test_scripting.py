from typing import Final
import mock
import pytest
import pandas as pd
import tempfile
import shutil
import os

from PWBM_Cloud_Utils import Model, Scenario, FilePath, run
from PWBM_Cloud_Utils.api_functions import ScenarioAPI

TEST_DIR: Final[str] = os.path.dirname(__file__)


class TestFilePath:

    # ---
    # .read()
    #
    # One with json file
    # The other with csv file
    # ---

    def test_read_json(self):
        fp = FilePath(os.path.join(TEST_DIR, "data/scenario/agi_surtax/runtime_options.json"))
        data = fp.read()

        assert data == {
            "stacking_order": "False",
            "first_year": 2019,
            "last_year": 2024,
            "mtr_vars": {
                "kg": [
                    "NetCapitalGainLongTerm"
                ]
            },
            "olg_inputs": "False",
            "dist_years": [
                2023
            ],
            "numba_mode": "True",
            "sample_rate": 0.1,
            "batch_size": 1,
            "run_baseline": "True",
        }

    def test_read_csv(self):
        fp = FilePath(os.path.join(TEST_DIR, "data/scenario/test_scenario/param_2.csv"))
        data = fp.read()

        assert data.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}))


class TestModel:

    # ---
    # .load()
    # ---

    def test_load_model(self):
        model = Model.load(99)

        assert model._id == 99

    # def test_create(self):
    #     # Mocking ModelsAPI class
    #     models_api_mock = MagicMock()
    #     # Mocking the response of create_model method
    #     response_data = {
    #         'name': 'test_name',
    #         'description': 'test_description',
    #         'git_repo': 'test_git_repo',
    #         'git_branch': 'test_git_branch',
    #         'id': 10000,
    #         'output_bucket': 'test_output_bucket',
    #         'job_queue': 'test_job_queue',
    #         'job_definition': 'test_job_definition',
    #         'compute_environment': 'test_compute_environment',
    #         'ecr_registry': 'test_ecr_registry',
    #         'version': 'test_version',
    #         'created': 'test_created',
    #         'modified': 'test_modified'
    #     }
    #     models_api_mock.create_model.return_value = response_data

    #     # Calling the method under test
    #     model_instance = Model.create('test_name', 'test_description', 'test_git_repo', 'test_git_branch', models_api_mock)

    #     # Assertions
    #     assert model_instance._id == 10000


@pytest.fixture()
def scenario_api() -> ScenarioAPI:
    scenario_api = mock.Mock()
    scenario_api.execute_scenario.return_value = None
    scenario_api.create_scenario.return_value = {"id": -99}

    return scenario_api


@pytest.fixture()
def flat_scenario(scenario_api) -> Scenario:
    model = Model.load(104)
    objects = {
        'param_1': {'a': 1, 'b': 2},
        'param_2': pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}),
    }

    return Scenario.new(model, objects, scenario_api)


@pytest.fixture()
def hierarchical_scenario(scenario_api) -> Scenario:
    model = Model.load(99)
    objects = {
        'param_1': {'a': 1, 'b': 2},
        'dir/param_2': pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}),
    }

    return Scenario.new(model, objects, scenario_api)


class TestScenario:
    # def test_init(self):
    #     fake_senario_io = 99
    #     fake_model_id = 99

    #     object_path = tempfile.TemporaryDirectory()
    #     shutil.copy('src/tests/data/read/csv file.csv', object_path.name)
    #     assert os.path.isfile(os.path.join(object_path.name, 'csv file.csv'))

    #     scenario = Scenario(fake_senario_io, fake_model_id, object_path)

    # ---
    # .load()
    # ---

    def test_load_scenario(self):
        scenario = Scenario.load(192)

        assert scenario["agi_surtax/runtime_options"] == {
            "stacking_order": "False",
            "first_year": 2019,
            "last_year": 2024,
            "mtr_vars": {
                "kg": [
                    "NetCapitalGainLongTerm"
                ]
            },
            "olg_inputs": "False",
            "dist_years": [
                2023
            ],
            "numba_mode": "True",
            "sample_rate": 0.1,
            "batch_size": 1,
            "run_baseline": "True",
        }

        assert scenario["agi_surtax/tax_law/1_percent/surtax"] == {
            "thresh_single": 15000,

            "thresh_mfs": 15000,

            "rate": {
                "2019": 0,
                "2023": 0.01,
            }
        }

    # ---
    # .new()
    # ---

    def test_new_with_flat_arrangement(self):
        model = Model.load(104)
        objects = {
            'param_1': {'a': 1, 'b': 2},
            'param_2': pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}),  
        }

        scenario = Scenario.new(model, objects)

        assert not scenario.is_on_cloud() 
        assert scenario['param_1'] == objects['param_1']
        assert scenario['param_2'].equals(objects['param_2'])

    def test_new_with_hierarchical_arrangement(self):
        model = Model.load(104)
        objects = {
            'param_1': {'a': 1, 'b': 2},
            'dir/param_2': pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}),
        }

        scenario = Scenario.new(model, objects)

        assert not scenario.is_on_cloud()
        assert scenario['param_1'] == objects['param_1']
        assert scenario['dir/param_2'].equals(objects['dir/param_2'])

    def test_new_with_filepath(self):
        """ This test mixes hierarchical arrangements with FilePath.
        """
        model = Model.load(104)
        objects = {
            'param_1': {'a': 1, 'b': 2},
            'param_2': pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}),
            'sub_dir/param_3': FilePath(os.path.join(TEST_DIR, 'data/scenario/agi_surtax/runtime_options.json')),
        }

        scenario = Scenario.new(model, objects)

        assert scenario['param_1'] == {'a': 1, 'b': 2}
        assert scenario['param_2'].equals(
            pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
        )
        assert scenario['sub_dir/param_3'] == {
            "stacking_order": "False",
            "first_year": 2019,
            "last_year": 2024,
            "mtr_vars": {
                "kg": [
                    "NetCapitalGainLongTerm"
                ]
            },
            "olg_inputs": "False",
            "dist_years": [
                2023
            ],
            "numba_mode": "True",
            "sample_rate": 0.1,
            "batch_size": 1,
            "run_baseline": "True",
        }

    # ---
    # .clone()
    # ---

    def test_clone_without_overrides(self, flat_scenario):
        cloned_scenario = flat_scenario.clone()

        assert not cloned_scenario.is_on_cloud()
        assert cloned_scenario["param_1"] == {'a': 1, 'b': 2}
        assert cloned_scenario["param_2"].equals(pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}))

    # TODO: can we ensure that flat_scenario.is_on_cloud() is True, so that we can
    #       check that it is changing?
    def test_clone_with_overrides(self, flat_scenario):
        new_param_1 = {'a': 10, 'b': 30}
        assert flat_scenario["param_1"] != new_param_1  # checking assumptions

        cloned_scenario = flat_scenario.clone(objects_to_override={"param_1": new_param_1})

        assert not cloned_scenario.is_on_cloud()
        assert cloned_scenario["param_1"] == new_param_1
        assert cloned_scenario["param_2"].equals(pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}))

    def test_clone_with_hierarchical_overrides(self, hierarchical_scenario):
        new_param_2 = pd.DataFrame({'a': [10, 20, 30], 'b': [30, 40, 50]})
        assert not hierarchical_scenario["dir/param_2"].equals(new_param_2)  # checking assumptions

        cloned_scenario = hierarchical_scenario.clone(objects_to_override={"dir/param_2": new_param_2})

        assert not cloned_scenario.is_on_cloud()
        assert cloned_scenario["param_1"] == {'a': 1, 'b': 2}
        assert cloned_scenario["dir/param_2"].equals(new_param_2)

    # ---
    # .__del__()
    # ---

    def test_del_clears_directory(self):
        fake_senario_io = 99
        fake_model_id = 99

        object_path = tempfile.TemporaryDirectory()
        shutil.copy(os.path.join(TEST_DIR, 'data/read/csv file.csv'), object_path.name)
        assert os.path.isfile(os.path.join(object_path.name, 'csv file.csv'))

        scenario = Scenario(fake_senario_io, fake_model_id, object_path)

        # Action:
        del scenario

        assert not os.path.isfile(os.path.join(object_path.name, 'csv file.csv'))
        assert not os.path.isdir(object_path.name)

    # ---
    # .__getitem__()
    # ---

    def test_get_for_flat_scenario(self, flat_scenario):
        assert flat_scenario['param_1'] == {'a': 1, 'b': 2}
        assert flat_scenario['param_2'].equals(
            pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
        )

    def test_get_subvalues_for_flat_scenario(self, flat_scenario):
        assert flat_scenario['param_1']['a'] == 1
        assert flat_scenario['param_2']['a'].equals(
            pd.Series([1, 2, 3])
        )

    def test_get_for_hierarchical_scenario(self, hierarchical_scenario):
        assert hierarchical_scenario['param_1'] == {'a': 1, 'b': 2}
        assert hierarchical_scenario['dir/param_2'].equals(
            pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
        )

    def test_get_subvalues_for_hierarchical_scenario(self, hierarchical_scenario):
        assert hierarchical_scenario['param_1']['a'] == 1
        assert hierarchical_scenario['dir/param_2']['a'].equals(
            pd.Series([1, 2, 3])
        )

    @pytest.mark.skip
    def test_set_val_by_get(self):
        """ .is_on_cloud() should be false if a value is changed through .__getitem__().
        """
        pass

    # ---
    # ._read_directory_data()
    # ---

    def test_read_directory_data_for_flat_scenario(self, flat_scenario):
        data = flat_scenario._read_directory_data()

        assert data["param_1"] == {'a': 1, 'b': 2}
        assert data["param_2"].equals(pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}))

    def test_read_directory_data_for_hierarchical_scenario(self, hierarchical_scenario):
        data = hierarchical_scenario._read_directory_data()

        assert data["param_1"] == {'a': 1, 'b': 2}
        assert data["dir/param_2"].equals(pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}))

    # ---
    # ._read_file_data()
    # ---

    def test_read_file_data_json(self):
        data = Scenario._read_file_data(os.path.join(TEST_DIR, 'data/scenario/test_scenario/param_1.json'))

        assert data == {'a': 1, 'b': 2}

    def test_read_file_data_csv(self):
        data = Scenario._read_file_data(os.path.join(TEST_DIR, 'data/scenario/test_scenario/param_2.csv'))

        assert data.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}))

    # ---
    # .__setitem__()
    # ---

    def test_set_for_flat_scenario(self, flat_scenario):
        new_param_1 = {'a': 30, 'b': 20}
        assert flat_scenario['param_1'] != new_param_1  # checking assumptions

        flat_scenario['param_1'] = new_param_1

        assert flat_scenario['param_1'] == new_param_1
        assert flat_scenario['param_2'].equals(
            pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
        )

    def test_set_for_hierarchical_scenario(self, hierarchical_scenario):
        new_param_2 = pd.DataFrame({'a': [10, 20, 30], 'b': [3, 4, 5]})
        assert not hierarchical_scenario['dir/param_2'].equals(new_param_2)  # checking assumptions

        hierarchical_scenario['dir/param_2'] = new_param_2

        assert hierarchical_scenario['param_1'] == {'a': 1, 'b': 2}
        assert hierarchical_scenario['dir/param_2'].equals(new_param_2)

    def test_set_for_flat_scenario_with_filepath(self, flat_scenario):
        new_param_1 = {
            "stacking_order": "False",
            "first_year": 2019,
            "last_year": 2024,
            "mtr_vars": {
                "kg": [
                    "NetCapitalGainLongTerm"
                ]
            },
            "olg_inputs": "False",
            "dist_years": [
                2023
            ],
            "numba_mode": "True",
            "sample_rate": 0.1,
            "batch_size": 1,
            "run_baseline": "True",
        }
        assert flat_scenario['param_1'] != new_param_1  # checking assumptions

        flat_scenario['param_1'] = FilePath(os.path.join(TEST_DIR, 'data/scenario/agi_surtax/runtime_options.json'))

        assert flat_scenario['param_1'] == new_param_1
        assert flat_scenario['param_2'].equals(
            pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
        )

    # ---
    # ._push()
    # ---

    def test_push_flat_arrangement(self, flat_scenario):
        assert not flat_scenario.is_on_cloud()

        flat_scenario._push()

        assert flat_scenario.is_on_cloud()

    def test_push_hierarchical_arrangement(self, hierarchical_scenario):
        assert not hierarchical_scenario.is_on_cloud()

        hierarchical_scenario._push()

        assert hierarchical_scenario.is_on_cloud()

    def test_not_push_existing_scenario(self, scenario_api):
        """ ._push() is not called for a scenario on the cloud.
        """
        scenario = Scenario.load(62)
        assert scenario.is_on_cloud()  # check assumption
        model = Model.load(scenario.model_id)

        scenario._push = mock.Mock()

        # Action:
        run(model, [scenario], scenario_api=scenario_api)

        scenario._push.assert_not_called()

    # ---
    # run():
    # ---

    @pytest.mark.skip
    def test_new_and_run_with_nested_arrangement(self):
        """ This test serves as an end-to-end test without mocking.
        """
        # we need to change zip_file_name = f"agi_surtax" in_push method in order to run
        # this unit test successfully
        model = Model.load(104)
        objects = {
            "behavioral_assumptions": {
                "1_percent": {
                    "elasticities": {
                        "kg": {
                            "variables": ["NetCapitalGainLongTerm"],
                            "value": -2.5,
                            "type": 4,
                        }
                    }
                }
            },
            "runtime_options": {
                "stacking_order": "False",
                "first_year": 2019,
                "last_year": 2024,
                "mtr_vars": {
                    "kg": [
                        "NetCapitalGainLongTerm"
                    ]
                },
                "olg_inputs": "False",
                "dist_years": [
                    2023
                ],
                "numba_mode": "True",
                "sample_rate": 0.1,
                "batch_size": 1,
                "run_baseline": "True",
            },
            "tax_law/1_percent/surtax": {
                "thresh_single": 15000,
                "thresh_mfs": 15000,
                "rate": {
                    "2019": 0,
                    "2023": 0.01,
                }
            },
        }

        scenario = Scenario.new(model, objects)

        assert scenario["tax_law/1_percent/surtax"] == objects["tax_law/1_percent/surtax"]
        assert scenario["behavioral_assumptions"] == objects["behavioral_assumptions"]

        run(model, [scenario])

    def test_not_run_with_inconsistent_model_id(self, scenario_api):

        scenario = Scenario.load(62)
        model = Model.load(99)

        with pytest.raises(ValueError) as e:
            run(model, [scenario], scenario_api=scenario_api)
        assert str(e.value) == "Scenario's model ID and model's ID don't match."
