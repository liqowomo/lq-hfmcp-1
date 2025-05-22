# This python file is for creating and uploading files to huggingface

from src.utz import header1, header2
import os
from dotenv import load_dotenv
from huggingface_hub import create_repo, SpaceHardware, SpaceStorage, upload_file

# Loading the env file
load_dotenv("src/.env")
hf_token = os.getenv("HF")


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
    - token (str): Hugging Face token for authentication. 
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
    repo_name = "Liqo/MakefromPy2"

    # Create the repository
    make_repo_model = create_repo(
        repo_id=repo_name, 
        repo_type="model", 
        token=hf_token
    )

    header2(f"{repo_name}")
    return make_repo_model

# --- Uploading files to repo ---

def hf_upload_files():
    """
    Upload a file to a Hugging Face repository.

    Parameters:
    - local_path (str): Path to local file to upload
    - remote_path (str): Path inside the repo (e.g., "folder/filename.txt")
    - repo_id (str): Repo name in "namespace/repo" format
    - repo_type (str): One of "model", "dataset", or "space"
    - commit_message (str): Commit summary
    - commit_description (str): Optional full commit description
    - create_pr (bool): Whether to open a Pull Request (default: False)

    Returns:
    - CommitInfo or Future: The result of the upload
    """

    upload_filez = upload_file(
        path_or_fileobj="src/utz.py",
        path_in_repo="utz.py",
        repo_id="Liqo/MakefromPy2",
        token=hf_token,
        repo_type="model",
        commit_message="Added utz.py",
        commit_description="Added utz.py",
        create_pr=False
    )
    header2(f"Uploading file to {upload_filez}")
    return upload_filez

