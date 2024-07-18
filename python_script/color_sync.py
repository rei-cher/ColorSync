import tkinter as tk
from tkinter import ttk
import serial
import time
from threading import Thread
from components.solid_color import SolidColor
from components.screen_color_sync_ui import ScreenColorSyncUI
from components.snake import Snake
from components.rainbow import Rainbow
from screen_color_sync import ScreenColorSync

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 115200

color_sync = None

def send_command(command):
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            ser.write((command + '\n').encode())
            time.sleep(0.1)
            print(f"Sent command: {command}")
    except serial.SerialException as e:
        print(f"Error communicating with serial port: {e}")

def start_color_sync(screen_index):
    global color_sync
    if color_sync is not None:
        color_sync.stop()
    color_sync = ScreenColorSync(SERIAL_PORT, BAUD_RATE, screen_index, sync_interval=0.1, smoothing_factor=0.3)
    thread = Thread(target=color_sync.start)
    thread.start()

def stop_color_sync():
    global color_sync
    if color_sync:
        color_sync.stop()
        color_sync = None
    send_command("off")

def on_closing():
    stop_color_sync()
    root.destroy()

def show_screen_color_sync():
    clear_content_frame()
    ScreenColorSyncUI(content_frame, start_color_sync)

def show_solid_color():
    clear_content_frame()
    SolidColor(content_frame, send_command)

def show_snake():
    clear_content_frame()
    Snake(content_frame, send_command)

def show_rainbow():
    clear_content_frame()
    Rainbow(content_frame, send_command)

def clear_content_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def main():
    global root, content_frame
    root = tk.Tk()
    root.title("RGB Pattern Control")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry("800x500")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12), padding=10)
    style.configure('TLabel', font=('Helvetica', 12), padding=10)
    style.configure('TRadiobutton', font=('Helvetica', 12), padding=5)

    sidebar_frame = ttk.Frame(root, width=200, style='TFrame')
    sidebar_frame.pack(expand=False, fill='both', side='left', anchor='nw')

    content_frame = ttk.Frame(root, style='TFrame')
    content_frame.pack(expand=True, fill='both', side='right')

    ttk.Button(sidebar_frame, text="Screen Color Sync", command=show_screen_color_sync, width=20).pack(pady=10)
    ttk.Button(sidebar_frame, text="Solid Color", command=show_solid_color, width=20).pack(pady=10)
    ttk.Button(sidebar_frame, text="Snake", command=show_snake, width=20).pack(pady=10)
    ttk.Button(sidebar_frame, text="Rainbow", command=show_rainbow, width=20).pack(pady=10)
    ttk.Button(sidebar_frame, text="OFF", command=stop_color_sync, width=20).pack(pady=10)

    exit_button = ttk.Button(root, text="Exit", command=on_closing, width=20)
    exit_button.pack(side='bottom', pady=20, padx=100)

    root.mainloop()

if __name__ == "__main__":
    main()
