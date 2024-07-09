import tkinter as tk
import serial
import time

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 115200

def send_command(command):
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            ser.write((command + '\n').encode())
            time.sleep(0.1)
            print(f"Sent command: {command}")
    except serial.SerialException as e:
        print(f"Error communicatuing with serial port: {e}")

def main():
    root = tk.Tk()
    root.title("RGB Pattern Control")

    tk.Button(root, text="Fill Red", command=lambda: send_command("fillRed")).pack(pady=10)    
    tk.Button(root, text="Rainbow", command=lambda: send_command("rainbow")).pack(pady=10)
    tk.Button(root, text="Snake", command=lambda: send_command("snake")).pack(pady=10)
    tk.Button(root, text="OFF", command=lambda: send_command("off")).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()