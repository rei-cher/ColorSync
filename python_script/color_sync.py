import tkinter as tk
import serial
import time
from threading import Thread
from screen_color_sync import ScreenColorSync
from screeninfo import get_monitors

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

def main():
    global root
    root = tk.Tk()
    root.title("RGB Pattern Control")
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # List available screens
    screens = get_monitors()
    screen_var = tk.IntVar(value=0)

    tk.Label(root, text="Select Screen:").pack(pady=5)
    for i, screen in enumerate(screens):
        tk.Radiobutton(root, text=f"Screen {i} ({screen.width}x{screen.height})", variable=screen_var, value=i).pack(anchor='w')

    tk.Button(root, text="Fill Red", command=lambda: send_command("fillRed")).pack(pady=10)
    tk.Button(root, text="Rainbow", command=lambda: send_command("rainbow")).pack(pady=10)
    tk.Button(root, text="Snake", command=lambda: send_command("snake")).pack(pady=10)
    tk.Button(root, text="OFF", command=stop_color_sync).pack(pady=10)
    tk.Button(root, text="Start Color Sync", command=lambda: start_color_sync(screen_var.get())).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()