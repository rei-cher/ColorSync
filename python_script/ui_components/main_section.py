import customtkinter as ctk
from ui_components.additions.rgb_wheel import RGBWheel

class MainSection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = ctk.CTkLabel(self, text="Main Section", width=200, height=50)
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.rgb_wheel = None

        # Log the background color of the app
        self.log_background_color()

    def log_background_color(self):
        # Get the background color from the customtkinter theme
        bg_color = self.cget("fg_color")
        print(f"Main section background color of the app: {bg_color}")

    def display_rgb_wheel(self):
        self.clear_section()
        self.rgb_wheel = RGBWheel(self)

    def clear_section(self):
        for widget in self.winfo_children():
            widget.destroy()
