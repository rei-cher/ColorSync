from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import colorsys

class RGBWheel:
    @staticmethod
    def display(parent):
        fig, ax = plt.subplots(figsize=(5, 5), dpi=100)

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
                    rgb[j, i, 3] = 0  # Set alpha to 0 for background

        ax.imshow(rgb, extent=[-1, 1, -1, 1], origin='lower')
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title('2D RGB Color Wheel')

        # Remove background and borders
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_facecolor((1, 1, 1, 0))

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)
