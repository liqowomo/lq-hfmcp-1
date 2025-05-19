# This demos is copied from 
# https://www.gradio.app/playground 

from src.g1 import g1_main # Main gradio function herex
from src.ver1 import ver1_main # Get Versions

def main():
    ver1_main()
    g1_main()


if __name__ == "__main__":
    main()