# Custom GPT-4o Chatbot

This is a simple Gradio-powered chatbot built using OpenAI's GPT-4o model. You can define your own chatbot's behavior via a system prompt at launch.

## Features
- Set your chatbot's personality using a custom system message
- Chat with it through a clean Gradio interface
- Powered by OpenAI's `gpt-4o` model

## Setup

1. Clone this repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a .env file and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your-api-key-here
   ```
4. Run the app:
   ```bash
   python main.py
   ```

## Example
You'll be prompted to define the chatbot (e.g., "You are a helpful therapist"), and then the chat interface will launch in your browser.
