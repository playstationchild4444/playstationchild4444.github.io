import js
import json
import os
from pyodide.ffi import create_proxy
from flask import Flask,render_template
import json

app = Flask(__name__)

@app.route("/",methods=["GET"])
def somthing():
    return render_template("index.html")

if __name__ =="__main__":
    app.run()
    
chat_data = []  # Initialize empty chat history for the session

def add_message(role, content):
    js.document.getElementById('chat-log').innerHTML += f"<div><strong>{role.capitalize()}:</strong> {content}</div>"

def send_message():
    user_input = js.document.getElementById('user-input').value
    if user_input.strip().lower() in ["goodbye", "exit"]:
        add_message("user", user_input)
        add_message("chatbot", "Goodbye!")
        chat_data.append({"role": "user", "content": user_input})
        chat_data.append({"role": "chatbot", "content": "Goodbye!"})
        js.document.getElementById('user-input').value = ""
        return

    add_message("user", user_input)
    chat_data.append({"role": "user", "content": user_input})

    js.window.fetch_response(user_input, os.getenv("CHAT_GBT_API"))

def on_send_button_click(event):
    send_message()

def on_key_press(event):
    if event.key == "Enter":
        if event.shiftKey:
            return
        else:
            event.preventDefault()
            send_message()


send_button = js.document.getElementById('send-btn')
send_button.addEventListener('click', create_proxy(on_send_button_click))

user_input = js.document.getElementById('user-input')
user_input.addEventListener('keypress', create_proxy(on_key_press))


def handle_message(event):
    try:
        if isinstance(event.data, str):
            data = json.loads(event.data)
            if isinstance(data, dict):
                if data.get("type") == "response_message":
                    add_message("chatbot", data.get("text", ""))
                elif data.get("type") == "response_error":
                    add_message("chatbot", data.get("text", ""))
                else:
                    add_message("chatbot", "Received unexpected message type.")
            else:
                add_message("chatbot", "Received unexpected message format.")
        else:
            add_message("chatbot", "Received non-string message data.")
    except json.JSONDecodeError as e:
        add_message("chatbot", "Failed to parse message data.")

js.window.addEventListener('message', create_proxy(handle_message))

# Initialize chat log with previous history (empty now)
for message in chat_data:
    add_message(message["role"], message["content"])
