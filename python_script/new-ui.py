import customtkinter as ctk
import sys
from ui_components.left_section import LeftSection
from ui_components.main_section import MainSection

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("RGB Control")
        self.geometry("800x600")
        self.resizable(False, False)  # Disable window resizing

        self.grid_columnconfigure(0, weight=0)  # Left section fixed width
        self.grid_columnconfigure(1, weight=1)  # Main section expands horizontally
        self.grid_rowconfigure(0, weight=1)  # Allow sections to expand vertically

        self.main_section = MainSection(self)
        self.main_section.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.left_section = LeftSection(self, self.main_section)
        self.left_section.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

        # Log the background color of the app
        self.log_background_color()

        # Bind the close button event to the custom close method
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def log_background_color(self):
        # Get the background color from the customtkinter theme
        bg_color = self.cget("fg_color")
        print(f"Background color of the app: {bg_color}")

    def on_closing(self):
        sys.exit()

if __name__ == "__main__":
    app = App()
    app.mainloop()
