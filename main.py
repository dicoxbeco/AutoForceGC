import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Controller 

delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='s')
stop_key = KeyCode(char='s')

mouse = Controller

class ClickMouse(threading.Thread):
    def _init_(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click()
                time.sleep(self.delay)
            time.sleep(0.1)