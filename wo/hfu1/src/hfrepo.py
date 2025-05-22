# This python file is for creating and uploading files to huggingface

from src.utz import header1, rprint
import os
from dotenv import load_dotenv
from huggingface_hub import create_repo, SpaceHardware, SpaceStorage

# Loading the env file 
load_dotenv(".env")
hf_token = os.getenv("HFTOKEN")

HFS = [
        {"key": "HFTOKEN", "value": hf_token}
    ]

# Main function that will call the sub functions
def hf_repo_ops():
    """
    Main function for Hugging Face repository operations.
    """
    hf_create_repo()

# --- Function for creating a repo --- 

def hf_create_repo():
    header1("Creating a Hugging Face Repository - Model")
    """
    Create a Hugging Face repository with secrets from an .env file.

    Parameters:
    - repo_id (str): A namespace (user or an organization) and a repo name separated by a /.
    - repo_type (str): Type of the repo ("model", "dataset", "space"). Default is "space".
    - private (bool): Whether to make the repo private. Default is False.
    - space_sdk (str): Choice of SDK to use if repo_type is "space". Default is "gradio".
    - space_hardware (SpaceHardware): Choice of hardware if repo_type is "space". Default is SpaceHardware.CPU_SMALL.
    - space_storage (SpaceStorage): Choice of persistent storage tier. Default is SpaceStorage.SMALL.
    - space_sleep_time (int): Number of seconds of inactivity to wait before a Space is put to sleep.
    - env_file (str): Path to the .env file containing secrets. Default is ".env".
    """

    # Name of the repo 
    repo_name = "Liqo/but1"

    # Create the repository
    repo_url = create_repo(
        repo_id=repo_name,
        repo_type="model",
        space_secrets=HFS,
        token=hf_token 
    )

    rprint("Creating" + repo_name)
    return repo_url



