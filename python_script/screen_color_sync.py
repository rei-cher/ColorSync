import time
from PIL import ImageGrab
import serial
from screeninfo import get_monitors

class ScreenColorSync:
    def __init__(self, serial_port, baud_rate, screen_index, sync_interval=0.1, smoothing_factor=0.1):
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.screen_index = screen_index
        self.sync_interval = sync_interval
        self.smoothing_factor = smoothing_factor
        self.serial_conn = None
        self.capture_region = self.get_screen_region()
        self.running = True
        self.stopped = False
        self.previous_color = (0, 0, 0)
        self.brigtness = 255

    def get_screen_region(self):
        monitors = get_monitors()
        if self.screen_index < len(monitors):
            monitor = monitors[self.screen_index]
            left = min(monitor.x, monitor.x + monitor.width)
            top = min(monitor.y, monitor.y + monitor.height)
            right = max(monitor.x, monitor.x + monitor.width)
            bottom = max(monitor.y, monitor.y + monitor.height)
            return (left, top, right, bottom)
        else:
            raise ValueError("Invalid screen index")

    def get_average_color(self, image):
        image = image.resize((1, 1))
        return image.getpixel((0, 0))
    
    def compute_brightness(self, color):
        return int((color[0] + color[1] + color[2]) / 3)    

    def smooth_color(self, new_color):
        r = int(self.smoothing_factor * new_color[0] + (1 - self.smoothing_factor) * self.previous_color[0])
        g = int(self.smoothing_factor * new_color[1] + (1 - self.smoothing_factor) * self.previous_color[1])
        b = int(self.smoothing_factor * new_color[2] + (1 - self.smoothing_factor) * self.previous_color[2])
        self.previous_color = (r, g, b)
        return self.previous_color

    def send_color_to_esp32(self, color):
        if self.stopped:
            return
        r, g, b = color
        brightness = self.compute_brightness(color)
        color_str = f"rgb:{r},{g},{b}, b:{brightness}\n"
        if self.serial_conn:
            self.serial_conn.write(color_str.encode())
            print(f"Sent color: {color} with brightness: {brightness}")

    def turn_off_leds(self):
        if self.serial_conn:
            self.serial_conn.write("off\n".encode())
            print("Turned off LEDs")

    def start(self):
        try:
            self.serial_conn = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
            time.sleep(2)  # Wait for the serial connection to initialize
            while self.running:
                screen = ImageGrab.grab(self.capture_region)
                average_color = self.get_average_color(screen)
                smoothed_color = self.smooth_color(average_color)
                self.send_color_to_esp32(smoothed_color)
                time.sleep(self.sync_interval)
        except serial.SerialException as e:
            print(f"Serial error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.turn_off_leds()
            self.stopped = True
            if self.serial_conn:
                self.serial_conn.close()

    def stop(self):
        self.running = False
        self.stopped = True
