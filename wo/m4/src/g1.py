import time
import gradio as gr

def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.05)
        yield "You typed: " + message[: i + 1]

def create_chat_interface(echo_function, **kwargs):
    """Creates a Gradio ChatInterface with customizable parameters
    
    Args:
        echo_function: The function that processes messages
        **kwargs: Additional arguments for ChatInterface
        
    Returns:
        Configured ChatInterface instance
    """
    defaults = {
        "title": "Slow Booty Dance",
        "type": "messages",
        "flagging_mode": "manual",
        "flagging_options": ["Like", "Spam", "Inappropriate", "Other"],
        "save_history": True,
    }
    defaults.update(kwargs)
    
    return gr.ChatInterface(echo_function, **defaults)


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