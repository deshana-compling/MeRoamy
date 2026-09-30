import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_message
from tools import tools, toolcalls
import gradio as gr
from multimodal import tts_function

load_dotenv()

google_api_key = os.getenv('GEMINI_KEY')

openai = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=google_api_key
)

def chat(message, history):
    history = [{'role': h['role'],'content': h['content']} for h in history]
    messages = [{'role':'system', 'content': system_message}] + history + [{'role':'user','content': message}]
    response = openai.chat.completions.create(model='gemini-3.6-flash', messages=messages, tools=tools)
    
    while response.choices[0].finish_reason == 'tool_calls':
        message = response.choices[0].message
        responses = toolcalls(message)
        messages.append(message)
        messages.extend(responses)
        response = openai.chat.completions.create(model='gemini-3.6-flash', messages=messages, tools=tools)

    final_response = response.choices[0].message.content
    audio = tts_function(final_response)

    return final_response, audio

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    audio = gr.Audio(label='TravelAI voice response', autoplay=True)
    message = gr.Textbox(placeholder='Ask TravelAI about a destination...')

    def respond(user_message, history):
        response, audio_file = chat(user_message, history)

        history.append({'role':'user', 'content': user_message})
        history.append({'role':'assistant', 'content': response})

        return history, audio_file, ""

    message.submit(respond, inputs=[message, chatbot], outputs=[chatbot, audio, message])

demo.launch()