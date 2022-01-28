# importing time and threading
import time
import threading
from pynput.mouse import Button, Controller as mouseController
  
# pynput.keyboard is used to watch events of 
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Key, Controller as keyController, Listener, KeyCode
  
  
# variables are created to control the auto-clicker
mouseButton = Button.right
enterKey = Key.space
escKey = Key.esc
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='a')
  
# threading.Thread is used 
# to control clicks
class ReinforceNecklace(threading.Thread):
    
  # delay and button is passed in class 
  # to check execution of auto-clicker
    def __init__(self, mouseButton):
        super(ReinforceNecklace, self).__init__()
        self.mouseDelay = 0.001
        self.keyboardDelay1 = 0.1
        self.keyboardDelay2 = 0.1
        self.button = mouseButton
        self.running = False
        self.program_running = True
  
    def start_reinforcing(self):
        self.running = True
        print("Auto necklace reinforcement is running")
  
    def stop_reinforcing(self):
        self.running = False
        print("Auto necklace reinforcement is stopping")
  
    def exit(self):
        self.stop_reinforcing()
        self.program_running = False

    # method to check and run loop until 
    # it is true another loop will check 
    # if it is set to true or not, 
    # for mouse click it set to button 
    # and delay.
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.mouseDelay)
                # keyboard.press(enterKey)
                # time.sleep(self.keyboardDelay1)
                # keyboard.press(enterKey)
                # time.sleep(self.keyboardDelay1)
            time.sleep(0.1)
  
  
# instance of mouse controller is created
mouse = mouseController()
keyboard = keyController()
click_thread = ReinforceNecklace(mouseButton)
click_thread.start()
print("Auto necklace reinforcement starting...")
  
  
# on_press method takes 
# key as argument
def on_press(key):
    
  # start_stop_key will stop clicking 
  # if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_reinforcing()
        else:
            click_thread.start_reinforcing()
              
    # here exit method is called and when 
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()
  
  
with Listener(on_press=on_press) as listener:
    listener.join()