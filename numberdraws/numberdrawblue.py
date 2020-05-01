from tkinter import *
import torch, torchvision, os, cv2, time, multiprocessing, serial
from tkinter import ttk, Canvas
from numberevaluator import *
from PIL import Image, ImageDraw
import ctypes
import bluetooth

#bluetooth.discover_devices()

delay = .1
exitVar = True
connected = False
width = 400
height = 120
percent = 40
lastx, lasty = 0, 0

root = Tk()
root.configure(background="gray")

ser = serial.Serial('COM5', 9600, timeout=.4)

value = StringVar()
connectText = StringVar()
connectionColor = "green"
process = StringVar()

root.resizable(False, False)
canvas = Canvas(root, width=width, height=height)
canvas.create_line(40, 40, 360+2, 40, width=3)
canvas.create_line(40, 80, 360+2, 80, width=3)
canvas.create_line(40, 40, 40, 80, width=3)
canvas.create_line(360, 40, 360, 80, width=3)
canvas.grid(row=1, column=0, sticky=(N, W, E))
processLabel = Label(root, textvariable=process, height=1, font=("Arial", 22, "bold")).grid(row=2, column=0, sticky=(N, W, E))


def evaluate(event):
    global percent
    print("evalute")
    percent += 5
    ser.write(b'0')

def clear():
    print("clear")

def isConnected():
    ser.write(b'8')
    if (ser.read(7) == b'Connect'):
        return True
    else:
        return False

def checkConnection():
    global connectionColor, connected
    if (isConnected()):
        connectText.set("Connected:")
        connectionColor = "green"
        connected = True
    else: 
        connectText.set("Disconnected")
        connectionColor = "red"
        connected = False
    connectionLabel = Label(root, textvariable=connectText, height=1, font=("Arial", 36, "bold"), foreground=connectionColor).grid(row=0, column=0, sticky=(N, W, E))

def convertPercToPixels(percent):
    if (percent >= 100):
        return 360
    else:
        return ((percent/100)*320)+40


#---------------LOOPS---------------#
def Loop(): #techincally not a loop where the code run inside will not iterate, but this func reserved for the mainloop
    global value, connected
    run = True
    root.protocol("WM_DELETE_WINDOW", exitGUI)
    root.bind("<Button-1>", evaluate)
    print("Checking Connection...")
    while exitVar:
        root.update()
        if (not connected):
            checkConnection()
            pass
        pixels = convertPercToPixels(percent)
        value.set("Yes Sir!")
        process.set("hm")
        try:
            canvas.create_rectangle(40, 40, pixels, 80, fill="green")
        except:
            pass

def exitGUI():
    global exitVar
    exitVar = False
    root.destroy()

Loop()

    
    
