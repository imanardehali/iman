import tkinter as tk
from tkinter import messagebox
import pyautogui
import time

class BotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Configurable Game Bot")

        tk.Label(root, text="Seconds between clicks:").pack()
        self.interval_entry = tk.Entry(root)
        self.interval_entry.pack()
        self.interval_entry.insert(0, "5")

        self.start_btn = tk.Button(root, text="Start", command=self.start_bot)
        self.start_btn.pack()
        self.stop_btn = tk.Button(root, text="Stop", command=self.stop_bot)
        self.stop_btn.pack()

        self.running = False

    def start_bot(self):
        try:
            self.interval = float(self.interval_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid interval")
            return
        self.running = True
        self.root.after(100, self.loop)

    def loop(self):
        if not self.running:
            return
        pyautogui.click()
        self.root.after(int(self.interval * 1000), self.loop)

    def stop_bot(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = BotApp(root)
    root.mainloop()
