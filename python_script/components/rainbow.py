import tkinter as tk
from tkinter import ttk

class Rainbow:
    def __init__(self, parent, send_command):
        self.parent = parent
        self.send_command = send_command
        self.setup_ui()

    def setup_ui(self):
        ttk.Button(self.parent, text="Rainbow", command=lambda: self.send_command("rainbow")).pack(pady=10)
