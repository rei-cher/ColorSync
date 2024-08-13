from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import colorsys
import customtkinter as ctk

red, green, blue = 43, 43, 43
class RGBWheel:
    def __init__ (self, parent):
        self.parent = parent
        self.brightness = 1.0
        self.bg_color = (red/255, green/255, blue/255)
        self.wheel_diameter = 4.5
        self.y_padding = 0.2

        self.display()

    def display(self):
        fig, ax = plt.subplots(figsize=(self.wheel_diameter, self.wheel_diameter), dpi=100)

        # Set the figure and axes background to be a specific color
        fig.patch.set_facecolor(self.bg_color)  # Background color of the figure
        ax.set_facecolor(self.bg_color)  # Background color of the axes

        # Create RGB color wheel
        resolution = 400
        hsv = np.zeros((resolution, resolution, 3))
        mask = np.zeros((resolution, resolution), dtype=bool)
        for i in range(resolution):
            for j in range(resolution):
                x = (2 * i / resolution) - 1
                y = (2 * j / resolution) - 1
                angle = np.arctan2(y, x) + np.pi
                radius = np.sqrt(x**2 + y**2)
                if radius <= 1:
                    hsv[j, i] = [angle / (2 * np.pi), radius, 1]
                else:
                    mask[j, i] = True  # Mark as outside the wheel

        # Convert HSV to RGB
        rgb = np.zeros((resolution, resolution, 4))  # Include alpha channel
        for i in range(resolution):
            for j in range(resolution):
                if not mask[j, i]:  # Only convert points within the wheel
                    rgb[j, i, :3] = colorsys.hsv_to_rgb(*hsv[j, i])
                    rgb[j, i, 3] = 1  # Set alpha to 1 for inside the wheel
                else:
                    rgb[j, i, 3] = 0  # Set alpha to 0 for outside the wheel

        # Render the RGB wheel
        ax.imshow(rgb, extent=[-1, 1, -1, 1], origin='lower')

        # Customize axes to remove borders and ticks
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1 - self.y_padding, 1 + self.y_padding)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title('Color Picker', color='white')

        # Remove background and borders
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        canvas = FigureCanvasTkAgg(fig, master=self.parent)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)

        # Create a circle to represent the selected color
        selected_color_circle, = ax.plot([0], [0], 'o', markersize=10, markeredgecolor='black', markeredgewidth=2, markerfacecolor='white')

        # Function to handle click event on the color wheel
        def on_click(event):
            # Convert click position to data coordinates
            x = event.xdata
            y = event.ydata
            if x is not None and y is not None:
                # Calculate angle and radius to determine the HSV values
                angle = np.arctan2(y, x) + np.pi
                radius = np.sqrt(x**2 + y**2)
                if radius <= 1:
                    h = angle / (2 * np.pi)
                    s = radius
                    v = 1
                    r, g, b = colorsys.hsv_to_rgb(h, s, v)
                    r = int(r * 255)
                    g = int(g * 255)
                    b = int(b * 255)
                    print(f"Your color is - r:{r}, g:{g}, b:{b}")

                    # Update the position and color of the circle
                    selected_color_circle.set_data([x], [y])
                    selected_color_circle.set_markerfacecolor((r/255, g/255, b/255))
                    fig.canvas.draw()

        # Connect the click event to the on_click function
        fig.canvas.mpl_connect('button_press_event', on_click)

        # Add a brightness scrollbar
        self.brightness_scale = ctk.CTkSlider(master = self.parent, from_ = 0, to = 1, number_of_steps = 100, command = self.update_brightness)
        self.brightness_scale.set(self.brightness)
        self.brightness_scale.grid(row = 1, column = 0, padx = 20, pady = 10)

    def update_brightness(self, value):
        self.brightness = float(value)
        self.display()