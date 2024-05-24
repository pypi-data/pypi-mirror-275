import os
import pytest

from PWBM_Cloud_Utils import (
    is_local_execution, is_cloud_execution,
)

ENV_VAR_NAME = "CLOUD_EXECUTION"


@pytest.fixture()
def setup_environment():
    old_value = os.environ.pop(ENV_VAR_NAME, None)

    yield

    if old_value is not None:
        os.environ[ENV_VAR_NAME] = old_value


def test_is_local_and_cloud_execution_for_local_run(setup_environment):
    os.environ[ENV_VAR_NAME] = "FALSE"

    assert is_local_execution()
    assert not is_cloud_execution()


def test_is_local_and_cloud_execution_for_cloud_run(setup_environment):
    os.environ[ENV_VAR_NAME] = "TRUE"

    assert not is_local_execution() 
    assert is_cloud_execution()
