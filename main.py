from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import filedialog as fd
from PIL import Image, ImageDraw, ImageTk, ImageFont
from random import randint
import pyscreenshot
from tkinter import colorchooser, messagebox
from tkinter.messagebox import showinfo

root = Tk()
root.title('Visual Drawing')
root.geometry('1300x800')

def draw(event):
    x1, y1 = (event.x - brushSize), (event.y - brushSize)
    x2, y2 = (event.x + brushSize), (event.y + brushSize)
    window.create_oval(x1, y1, x2, y2, fill=brushColor, width=0)
    draw_img.ellipse((x1, y1, x2, y2), fill=brushColor, width=0)

def erase(event):
    x1, y1 = (event.x - eraseSize), (event.y - eraseSize)
    x2, y2 = (event.x + eraseSize), (event.y + eraseSize)
    window.create_oval(x1, y1, x2, y2, fill=erase_color, width=0)
    draw_img.ellipse((x1, y1, x2, y2), fill=erase_color, width=0)

def open_image():
    global img, img_tk, draw
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    img_tk = ImageTk.PhotoImage(img)
    window.config(width=img.width, height=img.height)
    window.create_image(0, 0, anchor=tk.NW, image=img_tk)
    draw = ImageDraw.Draw(img)


txt = Entry(root, width=30, bg='white')              
input_x = Entry(root, width=30, bg='white')        
input_y = Entry(root, width=30, bg='white')         
txt.place(x=930, y=10)
input_x.place(x=930, y=30)
input_y.place(x=930, y=50)
listbox = Listbox(root, width=11, height=5)
listbox.place(x=1125, y=35) 
listbox.insert(1,'brush-on') 
listbox.insert(2,'text-on')
listbox.insert(3,'colors-on')
listbox.insert(4,'status:\nactive')
listbox.insert(5, 'program-on')
vlist = ["обычная"]
 
Combo = ttk.Combobox(root, width=8, values = vlist)
Combo.set("Кисти")
Combo.place(x=1125, y=10)



def chooseColor():
    global brushColor
    (rgb, hx) = colorchooser.askcolor()
    brushColor = hx
    color_lab['bg'] = hx

def chooseFigureColor():
    global figureColor
    (rgb, hx) = colorchooser.askcolor()
    figureColor = hx
    color_figure['bg'] = hx

def chooseHolstColor():
    global holst_color
    (rgb, hx) = colorchooser.askcolor()
    holst_color = hx
    color_holst['bg'] = hx

def select(value):
    global brushSize
    brushSize = int(value)

def select_erase(value):
    global eraseSize
    eraseSize = int(value)

def select_figure(value):
    global figureSize
    figureSize = int(value)

def fill():
    window.delete('all')
    window['bg'] = holst_color
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill=holst_color)
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill=holst_color)

def clear():
    window.delete('all')
    window['bg'] = 'white'
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill='white')

def save_image():
    image = pyscreenshot.grab(bbox=None)
    image.show()
    image.save('screenshot.png')

def get():
    a = txt.get()
    b = input_x.get()
    c = input_y.get()
    window.create_text(b, c, text = a, fill='black', font=("Helvetica 15 bold"))

def save():
    filename = f'image{randint(0, 1000000000)}.png'
    image1.save(filename)
    messagebox.showinfo('Сохранение...', 'Сохранено под названием %s' % filename)
         

def popup(event):
    global x, y 
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

def square():
    window.create_rectangle(x, y, x + figureSize, y + figureSize, fill=figureColor, width=0)
    draw_img.polygon((x, y, x + figureSize, y , x + figureSize, y + figureSize, x, y + figureSize), fill=figureColor)

def circle():
    window.create_oval(x, y, x + figureSize, y + figureSize, fill=figureColor, width=0)
    draw_img.ellipse((x, y, x + figureSize, y + figureSize), fill=figureColor)

def triangle():
    window.create_line(x, y, x + figureSize, y + figureSize, fill=figureColor, width=0)
    draw_img.line((x, y, x + figureSize, y + figureSize), fill=figureColor)

def line():
    window.create_line(x, y,x + figureSize, y + figureSize, 200, 25, fill=figureColor, width=0)
    draw_img.line((x, y, x + figureSize, y + figureSize), fill=figureColor)

def line_prime():
    window.create_line(x, y, x + figureSize, y + figureSize, fill=figureColor, width=10)
    draw_img.line((x, x + figureSize), fill=figureColor)

def kvadrat():
    window.create_rectangle(x, y, x + figureSize, y + figureSize, fill=figureColor, width=0)
    draw_img.regular_polygon((x, y, x + figureSize, y , x + figureSize, y + figureSize, x, y + figureSize), fill=figureColor)



x = 0
y = 0



figureColor = 'black'
figureSize = 4
textSize = 5
eraseSize = 3
brushSize = 4
brushColor = 'black'
erase_color = 'white'
holst_color = 'black'

root.columnconfigure(6, weight=1)
root.rowconfigure(2, weight=1)
root.resizable(0, 0)
root.iconbitmap("icon.ico")

window = Canvas(root, bg='white')
window.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)


window.bind('<B1-Motion>',draw)
window.bind("<Button-1>")
window.bind('<B2-Motion>', erase)
window.bind('<Button-3>', popup)

menu = Menu(tearoff=0)
menu.add_command(label='Квадрат', command=square)
menu.add_command(label='Круг', command=circle)
menu.add_command(label='Линия(наклонная)', command=triangle)
menu.add_command(label='Линия(привязанная к верхней левой точке)', command=line)
menu.add_command(label='Линия(наклонная жирная)', command=line_prime)
menu.add_command(label='Прямоугольник', command=kvadrat)
image1 = Image.new('RGB', (1280, 640), 'white')
draw_img = ImageDraw.Draw(image1)



Button(root, text='Цвета', width=10, command=chooseColor).place(x=650, y=100)
Button(root, text='Цвет фигур:', width=10, command=chooseFigureColor).place(x=550, y=100)

color_lab = Label(root, bg=brushColor, width=11, height=4)
color_lab.place(x=650, y=20)
color_figure = Label(root, bg=figureColor, width=11, height=4)
color_figure.place(x=550, y=20)
color_holst = Label(root, bg=holst_color, width=15, height=4)
color_holst.place(x=20, y=20)

v = IntVar(value=10)
Scale(root, variable=v, from_=1, to=100, orient=HORIZONTAL, command=select).place(x=400, y=5)
t = IntVar(value=5)
Scale(root, variable=t, from_=1, to=100, orient=HORIZONTAL, command=select_erase).place(x=400, y=80)
c = IntVar(value=10)
Scale(root, variable=c, from_=1, to=300, orient=HORIZONTAL, command=select_figure).place(x=400, y=45)


Label(root, text='Размер кисти: ').place(x=300, y=25)
Label(root, text='Размер ластика:').place(x=300, y=100)
Label(root, text='Размер фигур: ').place(x=300, y=65)
Label(root, text='Залить опр. область\n(левая кнопка мыши)').place(x=150, y=90)
Button(root, text='Заливка холста\nвыбранным цветом', width=15, command=fill).place(x=20, y=90)
Button(root, text='Выбрать цвет\nзаливки', width=15, command=chooseHolstColor).place(x=160, y=40)
Button(root, text='Очистить\nхолст', width=10, command=clear, bg='red').grid(row=1, column=7)
Button(root, text='Сохранить\nпроект\n(без фото)', width=12, height=100, command=save, bg='magenta').grid(row=2, column=7, padx=7, pady=4)
Button(root, text='Сделать\nскриншот\nпроекта', width=10, height=5, command=save_image, bg='yellow').grid(row=0, column=7, padx=7)
Button(root, text='Импортировать фото', width=18, height=7, bg='orange', command=open_image).place(x=750, y=10)
Label(root, text='текст').place(x=890, y=10)
Label(root, text='x').place(x=910, y=30)
Label(root, text='y').place(x=910, y=50)
Button(root, text='Создать текст', width=20, command=get).place(x=945, y=90)


root.mainloop()
