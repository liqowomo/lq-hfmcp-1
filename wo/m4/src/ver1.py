# Function to the version of python and pip 
# Get the current python version

from .utz import rprint

import sys
import pkg_resources

def get_versions():
    python_version = sys.version
    pip_version = pkg_resources.get_distribution("pip").version
    return python_version, pip_version

def exec_get_versions():
    python_version, pip_version = get_versions()
    rprint(f"Python version: {python_version}")
    rprint(f"Pip version: {pip_version}")
