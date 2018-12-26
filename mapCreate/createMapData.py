import io
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.simpledialog
e1=[]
def callback(event):
    values = []
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    values.append(x)
    values.append(y)
    vectors.append(values)
    canvas.create_oval(x, y, x+4, y+4, fill="red")
    canvas.create_text(x+5, y, anchor=W, font=("Purisa", 20),
                   text=str(len(vectors)))

    print ("clicked at", x, y)

def getPoints():
    
    #adding the image
    File = askopenfilename(parent=root, initialdir="./",title='Select an image')
    print(File.split("/")[-1])
    image = Image.open(File)
    [imageSizeWidth, imageSizeHeight] = image.size
    #image = image.resize((int(imageSizeWidth/4), int(imageSizeHeight/4)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    global filename
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

    image.save("output.png")
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
frame=Frame(root,width=5700,height=4000)
frame.grid(row=2,column=30)
canvas = Canvas(frame,width=1000, height=1000, bg='black',scrollregion=(0,0,5700,4000))
getPoints()
print(vectors)

filename ="B2"
num = len(vectors)
floor = "B2"
area = "01"
macTitle = "00:23:A7:A6:00:"
macIp = "192.168.2."
x = "100"
y = "100"
x_range = "140"
y_range = "185"
isDeadEndEntry = ""

title = "\"floor_sensor_data\": [\n"
for i in range(num):
    now = i
    text = text +"  {\n"+"  \"floor\": \"" + floor + "\",\n" + "  \"area\": \"" + area + "\",\n" + "  \"sensor_id\": \"" + macTitle + str(i+1) + "\",\n"+ "  \"sensor_ip\": \"" + macIp + str(i+1) + "\",\n"+ "  \"seq_id\": \"" + str(i+1) + "\",\n"+ "  \"x\": \"" + str(vectors[now][0]) + "\",\n" + "  \"y\": \"" + str(vectors[now][1]) + "\",\n" + "  \"Next_N\": [\n    \"" + "Next_N"+ str(i+1) + "\"\n  ],\n"  + "  \"Pre_N\": [\n    \"" + "" + "\"\n  ],\n"+ "  \"T\": [\n    \"" + "T"+str(i+1) + "\"\n  ],\n"+ "  \"X_RANGE\": \"" + x_range + "\",\n" + "  \"Y_RANGE\": \"" + y_range + "\",\n"  + "  \"isDeadEndEntry\": \"" + isDeadEndEntry + "\"\n" + "}"
    if i != num-1:
        text = text + ",\n"
    else:
        text = title + text + "],\n"

#
#+ "{\n" +
#    "\"floor\":\"" + floor + "\","+
#        "\"area\":\"" + area + "\","+
#        "\"sensor_id\":\"" + "00:23:A7:A6:00:"+ i + "\","
    print(text)
f = open(filename+".txt", "w")
f.write(text)
