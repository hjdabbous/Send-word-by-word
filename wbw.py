import pyperclip
import pyautogui
import time
import tkinter as tk
from threading import Thread
import keyboard

class MessageSenderApp:
    def __init__(self, master):
        self.master = master
        master.title("Message spam HJD")

        self.label = tk.Label(master, text="Press F5 to start sending messages from clipboard.")
        self.label.pack(pady=10)

        keyboard.on_press_key("F5", self.start_sending)

    def start_sending(self, e):
        self.label.config(text="Sending messages...")
        clipboard_text = pyperclip.paste()
        words = clipboard_text.split()

        for word in words:
            send_message(word)

        self.label.config(text="Messages sent successfully.")

def send_message(word):
    pyperclip.copy(word)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(1)

def main():
    root = tk.Tk()
    app = MessageSenderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
