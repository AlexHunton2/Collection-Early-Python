from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0
storex, storey = 0, 0
width = 500
height = 500
distBetween = 20
points = []
first = True

#Definitions
def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def quadConvo(num):
    num = (((num * 12)/width) - 6)
    return num
    
def addLine(event):
    global lastx, lasty, storex, storey, first, points
    canvas.create_oval((lastx, lasty, event.x, event.y), width=5)
    lastx, lasty = event.x, event.y
    diffx, diffy = event.x - storex, event.y - storey
    if first:
        storex, storey = event.x, event.y
        first = False
    if (diffx > distBetween) or (diffx < -distBetween) or (diffy > distBetween) or (diffy < -distBetween):
        storex, storey = event.x, event.y
        canvas.create_oval((lastx, lasty, event.x, event.y), width=10, outline="red")
        points.append((quadConvo(event.x), quadConvo(event.y)))
        print(points)

#Root Create + Setup
root = Tk()
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Canvas Create + Setup
canvas = Canvas(root, width=width, height=height)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

#Main Loop
root.mainloop()