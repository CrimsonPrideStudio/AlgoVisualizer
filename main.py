import random
from tkinter import *
from tkinter import ttk
from bubbleSort import bubble
from heapSort import heapSort
from quikSort import quickSort

tk = Tk()
tk.title("ALAN")
tk.geometry("900x600+200+80")
tk.config(bg="#252525")


def draw(data, color_array):
    canvas.delete("all")
    C_height = 450
    C_width = 870
    x_width = C_width / (len(data) + 1)
    offset = 10
    sbr = 10
    n_data = [i / max(data) for i in data]

    for i, height in enumerate(n_data):
        x0 = i * x_width + offset + sbr
        y0 = C_height - height * 400
        x1 = (i + 1) * x_width
        y1 = C_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=("new roman", 13), fill="orange")

    tk.update_idletasks()


def startAlgo():
    if not data:
        return

    if reg_algo.get() == "Bubble Sort":
        bubble(data, draw, speedscale.get())

    elif reg_algo.get() == "QuickSort":
        quickSort(data, 0, len(data) - 1, draw, speedscale.get())
        draw(data, ["green" for x in range(len(data))])


def genrate():
    global data
    print("Selected Algorithm " + reg_algo.get())
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())
    data = []
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue, maxivalue + 1))
    draw(data, ['red' for x in range(len(data))])


reg_algo = StringVar()
lable1 = Label(tk, text="Algorithm", font=("Gretoon", 16), bg="#252525", width=10, fg="#40FFFF", relief=GROOVE, bd=1)
lable1.place(x=5, y=5)

algo_menu = ttk.Combobox(tk, width=12, font=("new roman", 14), textvariable=reg_algo,
                         values=["Bubble Sort", "QuickSort", "Insertion Sort", "Merge Sort", "Heap Sort"])
algo_menu.place(x=180, y=5)
algo_menu.current(0)

sizelable = Label(tk, text="Size: ", font=("arial", 14), bg="#252525", width=7, height=1, fg="#C040C0", relief=GROOVE,
                  bd=1)
sizelable.place(x=5, y=65)
sizevalue = Scale(tk, from_=0, to=30, orient=HORIZONTAL, font=("arial", 10), relief=GROOVE, width=6, bg="#FFC0FF")
sizevalue.place(x=100, y=60)

minlable = Label(tk, text="Min: ", font=("arial", 14), bg="#252525", width=7, height=1, fg="#C040C0", relief=GROOVE,
                 bd=1)
minlable.place(x=250, y=65)
minvalue = Scale(tk, from_=0, to=30, orient=HORIZONTAL, font=("arial", 10), relief=GROOVE, width=6, bg="#FFC0FF")
minvalue.place(x=350, y=60)

maxlable = Label(tk, text="Max: ", font=("arial", 14), bg="#252525", width=7, height=1, fg="#C040C0", relief=GROOVE,
                 bd=1)
maxlable.place(x=500, y=65)
maxvalue = Scale(tk, from_=1, to=100, orient=HORIZONTAL, font=("arial", 10), relief=GROOVE, width=6, bg="#FFC0FF")
maxvalue.place(x=600, y=60)

Genrate = Button(tk, text="Genrate", font=("arial", 15, "italic bold"), bg="#252525", fg="#FF0000", bd=1, width=10,
                 relief=SUNKEN, command=genrate)
Genrate.place(x=760, y=57)

start = Button(tk, text="Start", font=("arial", 15, "italic bold"), bg="#252525", fg="#FF0000", bd=1, width=10,
               relief=SUNKEN, command=startAlgo)
start.place(x=750, y=5)

speedlable = Label(tk, text="Time", font=("arial", 14), bg="#252525", width=7, fg="#C040C0", relief=GROOVE, bd=1)
speedlable.place(x=400, y=5)
speedscale = Scale(tk, from_=0.1, to=5.0, resolution=0.2, length=200, digits=2, orient=HORIZONTAL, font=("arial", 10),
                   relief=GROOVE, width=6, bg="#FFC0FF")
speedscale.place(x=520, y=5)

canvas = Canvas(tk, width=870, height=450, bg="#252525")
canvas.place(x=10, y=130)

tk.mainloop()
