import tkinter as tk
import subprocess

# Dictionary to keep track of subprocesses
processes = {}

def start_module(module_name, script_name):
    global processes
    if module_name not in processes or processes[module_name].poll() is not None:
        processes[module_name] = subprocess.Popen(["python", script_name])
    else:
        print(f"{module_name} module is already running.")

def on_key_press(event):
    key = event.char.lower()
    if key == 'f':
        start_module("Voice Assistant", "voice_assistant/speech.py")
    elif key == 'i':
        start_module("Voice Assistant by typing", "voice_assistant/main.py")
    elif key == 't':
        start_module("Text to Voice", "text_to_voice/main.py")
    elif key == 'j':
        start_module("Voice to Text", "voice_to_text/app.py")

# Create main window
root = tk.Tk()
root.title("Voice Assistant Application")

# Create buttons
btn_voice_assistant = tk.Button(root, text="Voice Assistant", command=lambda: start_module("Voice Assistant", "voice_assistant/speech.py"))
btn_voice_assistant.pack(pady=10)

btn_voice_assistant = tk.Button(root, text="Voice Assistant by typing", command=lambda: start_module("Voice Assistant", "voice_assistant/speech.py"))
btn_voice_assistant.pack(pady=10)

btn_text_to_voice = tk.Button(root, text="Text to Voice", command=lambda: start_module("Text to Voice", "text_to_voice/main.py"))
btn_text_to_voice.pack(pady=10)

btn_voice_to_text = tk.Button(root, text="Voice to Text", command=lambda: start_module("Voice to Text", "voice_to_text/app.py"))
btn_voice_to_text.pack(pady=10)

# Bind key presses to functions
root.bind('<KeyPress>', on_key_press)

# Run the application
root.mainloop()
