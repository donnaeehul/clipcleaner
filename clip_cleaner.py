import ctypes
import time
import tkinter as tk
from tkinter import messagebox


class ClipCleaner:
    def __init__(self, interval=60):
        self.interval = interval
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window
        self.last_clipboard_content = None

    def get_clipboard(self):
        try:
            return self.root.clipboard_get()
        except tk.TclError:
            return None

    def clear_clipboard(self):
        self.root.clipboard_clear()

    def check_clipboard(self):
        current_content = self.get_clipboard()
        if current_content != self.last_clipboard_content:
            self.last_clipboard_content = current_content
            print(f"Clipboard updated: {current_content}")

    def run(self):
        messagebox.showinfo("ClipCleaner", "ClipCleaner is now running in the background.")
        while True:
            self.check_clipboard()
            time.sleep(self.interval)


def main():
    cleaner = ClipCleaner()
    cleaner.run()


if __name__ == "__main__":
    main()