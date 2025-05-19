# This demos is copied from 
# https://www.gradio.app/playground 

from src.g1 import slow_echo, create_chat_interface

def main():
    g1_main()



def g1_main():
    # Create with default parameters
    demo = create_chat_interface(slow_echo)
    
    # Alternative with custom parameters:
    # demo = create_chat_interface(
    #     slow_echo,
    #     title="Custom Title",
    #     flagging_options=["Good", "Bad"]
    # )
    
    demo.launch()

if __name__ == "__main__":
    main()