# Function to the version of python and pip 
# Get the current python version

from .utz import rprint

import sys
import importlib.metadata  # Python 3.8+ standard library

def get_versions():
    """Returns Python and pip versions"""
    python_version = sys.version.split()[0]
    try:
        pip_version = importlib.metadata.version('pip')
    except importlib.metadata.PackageNotFoundError:
        pip_version = "Not available (UV environment?)"
    return python_version, pip_version

def exec_get_versions():
    """Executes and prints version information"""
    python_version, pip_version = get_versions()
    print(f"Python version: {python_version}")
    print(f"Pip version: {pip_version}")
