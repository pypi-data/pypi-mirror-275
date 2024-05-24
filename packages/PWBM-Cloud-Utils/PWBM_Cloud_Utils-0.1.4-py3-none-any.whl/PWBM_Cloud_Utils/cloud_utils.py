import argparse
from argparse import Namespace
from .io_config import IOConfig

def parse_args() -> Namespace:
    """
    Parses command-line arguments.

    Returns:
        Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scenario_id", help="Id of the scenario", type=int, required=False
    )
    return parser.parse_args()


def is_cloud_execution() -> bool:
    """
    Check if the execution environment is set to cloud.
    
    Returns:
        bool: True if execution is set to cloud, False otherwise.
    """
    return IOConfig().cloud_execution

def is_local_execution() -> bool:
    """
    Check if the execution environment is set to local.
    
    Returns:
        bool: True if execution is set to local, False otherwise.
    """
    return not IOConfig().cloud_execution


