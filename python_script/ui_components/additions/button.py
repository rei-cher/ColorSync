import customtkinter as ctk

class CustomButton(ctk.CTkButton):
    def __init__ (self, parent, text="Button", command=None, width=100, height=40, row=0, column=0, padx=0, pady=0):
        super().__init__(parent, text=text, command=command, width=width, height=height)
        self.row = row
        self.column = column
        self.padx = padx
        self.pady = pady

        self.configure(width=width, height=height)