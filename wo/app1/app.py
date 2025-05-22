# Creating the gradio mcp server from the tutorial 

import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text: str):