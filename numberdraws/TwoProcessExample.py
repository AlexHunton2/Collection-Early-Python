from tkinter import *
import torch, torchvision, os, cv2, time, multiprocessing
from tkinter import ttk
from numberevaluator import *
from PIL import Image, ImageDraw
import ctypes
import bluetooth

#bluetooth.discover_devices()

delay = .1
exitVar = True
width = 224
height = 224
lastx, lasty = 0, 0

root = Tk()
root.configure(background="gray")

global value
value = StringVar()

root.resizable(False, False)
canvas = Canvas(root, width=width, height=height)
label = Label(root, text="This is our first GUI!").grid(row=0, column=2, sticky=(N, W, E))
label = Label(root, textvariable=value).grid(row=1, column=4)
label = Label(root, textvariable=value).grid(row=2, column=5, sticky=(N, W, E))


def evaluate(event):
    print("evalute")
    root.update()

def clear():
    print("clear")


#---------------LOOPS---------------#
def tkinterLoop(v): #techincally not a loop where the code run inside will not iterate, but this func reserved for the mainloop
    global value
    run = True
    root.protocol("WM_DELETE_WINDOW", exitGUI)
    root.bind("<Button-1>", evaluate)
    while exitVar:
        root.update()
        value.set(str(v.value))

def blutetoothLoop(event, v):
    run = True
    while run:
        v.value = 56
        run = not event.is_set() #If the event is updated to true, then close the loop
        time.sleep(delay)
        print("hello")

def exitGUI():
    global exitVar
    exitVar = False
    root.destroy()

if __name__ == "__main__":
    event = multiprocessing.Event()
    value = multiprocessing.Value("i", 68)
    bluetoothProcess = multiprocessing.Process(name='bluetoothProcess', target=blutetoothLoop, args=(event, value))
    tkinterProcess = multiprocessing.Process(name='tkinterProcess', target=tkinterLoop, args=(value, ))

    tkinterProcess.start()
    bluetoothProcess.start()
    
    tkinterProcess.join()
    event.set() #Once the tkinter process is finished (the x is pressed), update the event to be True
    bluetoothProcess.join()
    
    
