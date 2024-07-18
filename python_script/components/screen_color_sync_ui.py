import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors

class ScreenColorSyncUI:
    def __init__(self, parent, start_color_sync):
        self.parent = parent
        self.start_color_sync = start_color_sync
        self.setup_ui()

    def setup_ui(self):
        screens = get_monitors()
        screen_var = tk.IntVar(value=0)

        center_frame = ttk.Frame(self.parent)
        center_frame.pack(expand=True, fill='both', pady=20)

        screen_select_frame = ttk.Frame(center_frame)
        screen_select_frame.pack(side='top', pady=10)

        tk.Label(screen_select_frame, text="Select Screen:").pack(pady=5)
        for i, screen in enumerate(screens):
            ttk.Radiobutton(screen_select_frame, text=f"Screen {i} ({screen.width}x{screen.height})", variable=screen_var, value=i).pack(anchor='w')

        ttk.Button(center_frame, text="Start Color Sync", command=lambda: self.start_color_sync(screen_var.get())).pack(pady=10)
