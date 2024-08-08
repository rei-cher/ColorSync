import customtkinter as ctk
from ui_components.additions.rgb_sphere import RGBSphere

class MainSection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = ctk.CTkLabel(self, text="Main Section", width=200, height=50)
        self.label.grid(row=0, column=0, padx=20, pady=20)

    def display_rgb_sphere(self):
        self.clear_section()
        RGBSphere.display(self)

    def clear_section(self):
        for widget in self.winfo_children():
            widget.destroy()
