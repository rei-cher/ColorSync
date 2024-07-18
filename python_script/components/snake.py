import tkinter as tk
from tkinter import ttk

class Snake:
    def __init__(self, parent, send_command):
        self.parent = parent
        self.send_command = send_command
        self.setup_ui()

    def setup_ui(self):
        ttk.Button(self.parent, text="Snake", command=lambda: self.send_command("snake")).pack(pady=10)
