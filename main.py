import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_msg = input("What kind of chatbot would you like to create?\n")
messages = [{'role': 'system', 'content': system_msg}]
print("Your new chatbot is ready! Launching the Gradio app...")

def chat_loop(user_input):
    messages.append({'role': 'user', 'content': user_input})
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': reply})
    return reply

gradio.Interface(
    fn=chat_loop,
    inputs=gradio.Textbox(label="Your message"),
    outputs=gradio.Textbox(label="Chatbot's reply"),
    title="Your Custom Chatbot",
    description="Talk to your chatbot below!",
).launch(share=True)