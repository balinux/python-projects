from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)
# keyboard.press('a')
# keyboard.release('a')

# keyboard.press(Key.cmd)
# keyboard.release(Key.cmd)

# menulis kalimat
# keyboard.type("halo saya yhotie")

# menulis kalimat pelan
for char in "halo saya yhotie":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)
