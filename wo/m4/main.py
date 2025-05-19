# This demos is copied from 
# https://www.gradio.app/playground 

from src.g1 import g1_main # Main gradio function herex
from src.ver1 import exec_get_versions # Get Versions

def main():
    exec_get_versions() # Get the versions of python and pip
    # g1_main()


if __name__ == "__main__":
    main()