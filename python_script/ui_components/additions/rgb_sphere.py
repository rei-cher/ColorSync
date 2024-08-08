from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class RGBSphere:
    @staticmethod
    def display(parent):
        fig = plt.figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        # Create RGB sphere
        phi, theta = np.mgrid[0.0:2.0*np.pi:100j, 0.0:np.pi:50j]
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)
        c = np.stack((x, y, z), axis=-1)

        # Normalize the color values to 0-1 range
        c = (c - c.min()) / (c.max() - c.min())
        
        ax.plot_surface(x, y, z, facecolors=c, rstride=1, cstride=1, antialiased=False)

        ax.set_xlabel('R')
        ax.set_ylabel('G')
        ax.set_zlabel('B')
        
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)
