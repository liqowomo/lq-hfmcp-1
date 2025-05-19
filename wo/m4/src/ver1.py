# Function to the version of python and pip 
# Get the current python version

from .utz import rprint

import sys 
import pkg_resources  # For pip version

def get_versions():
    """Returns Python and pip versions as a tuple"""
    python_version = sys.version.split()[0]  # Gets just the version number
    pip_version = pkg_resources.get_distribution("pip").version
    return python_version, pip_version

def exec_get_versions():
    """Executes and prints version information"""
    python_version, pip_version = get_versions()  # Unpack the tuple
    rprint(f"[bold]Python version:[/bold] {python_version}")
    rprint(f"[bold]Pip version:[/bold] {pip_version}")
