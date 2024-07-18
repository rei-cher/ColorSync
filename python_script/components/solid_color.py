import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import colorsys
import math

class SolidColor:
    def __init__(self, parent, send_command):
        self.parent = parent
        self.send_command = send_command
        self.last_color = (0, 0, 0)
        self.setup_ui()

    def setup_ui(self):
        self.canvas = tk.Canvas(self.parent, width=300, height=300)
        self.canvas.pack(pady=10)
        
        self.image = self.create_color_wheel(300)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
        self.canvas.bind("<Button-1>", self.on_color_select)
        self.canvas.bind("<B1-Motion>", self.on_color_select)

        self.brightness_scale = tk.Scale(self.parent, from_=0, to=100, orient='horizontal', label='Brightness', command=self.on_brightness_change)
        self.brightness_scale.set(50)  # Default brightness
        self.brightness_scale.pack(pady=10)
        
    def create_color_wheel(self, size):
        image = Image.new("RGB", (size, size))
        for y in range(size):
            for x in range(size):
                r, g, b = 0, 0, 0
                dx, dy = x - size / 2, y - size / 2
                dist = (dx ** 2 + dy ** 2) ** 0.5
                if dist <= size / 2:
                    hue = (math.atan2(dy, dx) / math.pi + 1) / 2
                    sat = dist / (size / 2)
                    r, g, b = [int(i * 255) for i in colorsys.hsv_to_rgb(hue, sat, 1)]
                image.putpixel((x, y), (r, g, b))
        return image

    def on_color_select(self, event):
        x, y = event.x, event.y
        if x < 0 or y < 0 or x >= 300 or y >= 300:
            return
        color = self.image.getpixel((x, y))
        self.last_color = color
        brightness = self.brightness_scale.get()
        self.send_command(f"fillSolid:{color[0]},{color[1]},{color[2]},b:{brightness}")
        print(f"Chosen color: {color[0]}, {color[1]}, {color[2]}, Brightness: {brightness}")

    def on_brightness_change(self, value):
        color = self.last_color
        self.send_command(f"fillSolid:{color[0]},{color[1]},{color[2]},b:{value}")
        print(f"Brightness set to: {value}")