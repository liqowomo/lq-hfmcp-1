import gradio as gr

MAIN_TEXT="""
# me1test1

1. Testing out markdown in the tab
"""

intro_page = gr.Interface(lambda: MAIN_TEST, inputs=None, outputs="markdown")
hello_world = gr.Interface(lambda name: "Hello " + name, "text", "text")
bye_world = gr.Interface(lambda name: "Bye " + name, "text", "text")
chat = gr.ChatInterface(lambda *args: "Hello " + args[0])

demo = gr.TabbedInterface(
    [intro_page, hello_world, bye_world, chat], 
    ["Intro Page", "Hello World", "Bye World", "Chat"]
    )

if __name__ == "__main__":
    demo.launch()
