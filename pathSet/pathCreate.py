import io
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.simpledialog


def callback(event):
    values = []
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    values.append(x)
    values.append(y)
    if len(vectors) > 0 :
        canvas.create_line(vectors[-1][0], vectors[-1][1], x, y)
    vectors.append(values)
    canvas.create_oval(x, y, x+4, y+4, fill="red")
    canvas.create_text(x+5, y, anchor=W, font=("Purisa", 20),
                           text=str(len(vectors)))
    print ("clicked at", x, y)

def getPoints():

    #adding the image
    File = askopenfilename(parent=root, initialdir="./",title='Select an image')
    print(File.split("/")[-1])
    img = ImageTk.PhotoImage(Image.open(File))
    filename = File.split("/")[-1]

    # load the .gif image file
    hbar=Scrollbar(frame,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM,fill=X)
    hbar.config(command=canvas.xview)
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=LEFT,expand=True,fill=BOTH)
    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
    canvas.create_image(0, 0, image=img, anchor=NW)
    canvas.bind("<Button-1>", callback)
    canvas.pack(side = "bottom", fill = "both", expand = "yes")

    root.mainloop()


def input_vector(axes):
    values = []
    string = "Enter the coordinate of "
    for coord in axes:
        values.append(int(input(string + coord)))
    return values



##########################===Main===############################
vectors = []
text =""

AXES = ('x : ', 'y : ')
root = Tk()
frame=Frame(root,width=4000,height=5700)
frame.grid(row=0,column=0)
canvas = Canvas(frame,width=1000, height=1000, bg='black',scrollregion=(0,0,4000,5700))
filename = "0M0002_B2"
getPoints()
print(vectors)


num = len(vectors)


for i in range(num):
    now = i
    next = i + 1
    if next >= num:
        next = 0
    step = abs((vectors[next][1] - vectors[now][1])) + abs(vectors[next][0] - vectors[now][0])
    step = (int)(step*0.2)
    for j in range(step):
        stepX = (int)(vectors[next][0] - vectors[now][0]) / step
        stepY = (int)(vectors[next][1] - vectors[now][1]) / step
        text = text + (str(vectors[i][0]+stepX*j)+","+str(vectors[i][1]+stepY*j))+"\n"
f = open(filename+".txt", "w")
f.write(text)
