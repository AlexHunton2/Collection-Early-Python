from tkinter import *
import torch, torchvision, os, cv2
from tkinter import ttk
from numberevaluator import *
from PIL import Image, ImageDraw

width = 224
height = 224
lastx, lasty = 0, 0
image = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_oval((lastx, lasty, event.x, event.y), width=3)
    draw.line([lastx, lasty, event.x, event.y], (0, 0, 0), width=3)
    lastx, lasty = event.x, event.y

root = Tk()
root.configure(background="gray")
root.resizable(False, False)
value = StringVar()
value.set("null")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root, width=width, height=height)
canvas.grid(column=1, row=4, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

label = Label(root, text="Prediction:").grid(row=0, column=0, sticky=(N, W, E))
label = Label(root, textvariable=value).grid(row=0, column=1, sticky=(N, W, E))

def evaluate():
    canvas.postscript(file="numberdraws\imgs\drawing.ps", colormode='color')
    image.save("numberdraws\imgs\drawing.png")
    updatedata = loaddata()
    value.set(updatedata)
    canvas.update()

def clear():
    canvas.delete('all')
    draw.rectangle([0, 0, width, height], (255, 255, 255))
    image.save("numberdraws\imgs\drawing.png")

button = Button(root, text="Evaluate", command=evaluate).grid(row = 2, column=0, sticky=(N, W, E))
clear = Button(root, text="Clear", command=clear).grid(row = 3, column=0, sticky=(N, W, E))

root.mainloop()