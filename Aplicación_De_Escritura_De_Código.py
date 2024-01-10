from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import os
import webbrowser

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("abrir.jpeg"))
save_img = ImageTk.PhotoImage(Image.open("guardar.jpeg"))
play_img = ImageTk.PhotoImage(Image.open("reproducir.jpeg"))

label_file_name = Label(root, text="Nombre del archivo: ")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text = Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name = ""

def openFile():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    html_file = filedialog.askopenfilename(title="Abrir Archivo H.T.M.L.", filetypes = (("Archivos H.T.M.L.", "*.html"), ))
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    html_file = open(name,'r')
    paragraph = html_file.read()
    my_text.insert(END,paragraph)
    html_file.close()
    
def save():
    input_name = input_file_name.get()
    file = open(input_name+".html","w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("Actualización","El archivo se a guardado exitosamente")
    
def run_html():
    global name
    webbrowser.open(name)

open_button = Button(root, image = open_img,text="Abrir archivo",command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button = Button(root, image = save_img,text="Guardar archivo",command=save)
save_button.place(relx=0.11,rely=0.03,anchor=CENTER)

play_button = Button(root, image = play_img,text="Reproducir archivo",command=run_html)
play_button.place(relx=0.17,rely=0.03,anchor=CENTER)


root.mainloop()