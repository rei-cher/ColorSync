import customtkinter as ctk
from ui_components.additions.button import CustomButton
import sys

class LeftSection(ctk.CTkFrame):
    def __init__(self, master, main_section):
        super().__init__(master)
        self.main_section = main_section
        
        self.grid_rowconfigure(3, weight=1)  # Allow the last row to expand
        
        # Screen Color Sync button
        self.screen_color_button = CustomButton(
            parent=self, 
            text="Color Sync with screen",
            width=200, 
            height=50, 
            row=0, 
            column=0, 
            padx=20, 
            pady=20
        )
        self.screen_color_button.grid(row=self.screen_color_button.row, column=self.screen_color_button.column, padx=self.screen_color_button.padx, pady=self.screen_color_button.pady)
        
        # Solid Color button
        self.solid_color_button = CustomButton(
            parent=self, 
            text="Solid Color",
            width=200, 
            height=50, 
            row=1, 
            column=0, 
            padx=20, 
            pady=20,
            command=self.display_rgb_wheel
        )
        self.solid_color_button.grid(row=self.solid_color_button.row, column=self.solid_color_button.column, padx=self.solid_color_button.padx, pady=self.solid_color_button.pady)

        # Patterns button
        self.patterns_button = CustomButton(
            parent=self, 
            text="Patterns",
            width=200, 
            height=50, 
            row=2, 
            column=0, 
            padx=20, 
            pady=20
        )
        self.patterns_button.grid(row=self.patterns_button.row, column=self.patterns_button.column, padx=self.patterns_button.padx, pady=self.patterns_button.pady)

        # Exit button
        self.exit_button = CustomButton(
            parent=self, 
            text="Exit",
            width=200, 
            height=50, 
            row=3, 
            column=0, 
            padx=20, 
            pady=20,
            command=self.exit_application
        )
        self.exit_button.grid(row=self.exit_button.row, column=self.exit_button.column, padx=self.exit_button.padx, pady=self.exit_button.pady, sticky='s')

    def display_rgb_wheel(self):
        self.main_section.display_rgb_wheel()

    def exit_application(self):
        sys.exit()
