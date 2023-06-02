from pynput.keyboard import Key, Controller
import webbrowser
import time
keyboard = Controller()
def split(words):
        return [char for char in words]
print(" ")
print("AUTOSRC by gparietti")
print(" ")
argument= input("what do you have to look for?")
time.sleep(1)
print(" ")
print("I'm looking for it for you...")
webbrowser.open("www.google.com")
time.sleep(3)
for i in split(argument):
    keyboard.type(i)
    time.sleep(.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print(" ")
print("My research ends here!")
time.sleep(1)
print(" ")
print("-an idea of gparietti-")
time.sleep(2)
#gparietti idea's
