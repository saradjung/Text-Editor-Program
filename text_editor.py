from tkinter import *
import os
from tkinter import filedialog, colorchooser, font
from tkinter.filedialog import *
from tkinter.messagebox import *

def change_color():
    color=colorchooser.askcolor(title="choose a color ")
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(),font_size.get()))



def copy():
    text_area.event_generate("<<Copy>>")

def cut():
    text_area.event_generate("<<Cut>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About this program","This is a text editor program created in pyhton GUI to edit your text files")

def new_file():
    window.title("Untitled")
    text_area.delete(1.0,END)


def open_file():
    #file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text files","*.txt")])
    filepath=filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text files","*.txt")])
    try:
    
        window.title(os.path.basename(filepath))
        text_area.delete(1.0,END)
        file=open(filepath,'r')
        text_area.insert(1.0,file.read())
    
    except Exception:
       print("File not found")

    finally:
      file.close()



def save_file():
    file=filedialog.asksaveasfilename(initialfile="untitled.txt",filetypes=[("All files","*.*"),("Text files","*.txt")])

    try:
        window.title(os.path.basename(file))
        file=open(file,'w')

        file.write(text_area.get(1.0,END))
    except Exception:
        print("couldnt save file")
    finally:
        file.close()



def exit():
    window.destroy()

window=Tk()
window.title("Text Editor")
window_width=500
window_height=500
#the following code is for centering the window
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
pos_x=int((screen_width/2)-(window_width/2))
pos_y=int((screen_height/2)-(window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width,window_height,pos_x,pos_y))

font_name=StringVar()
font_name.set('Consolas')

font_size=StringVar()
font_size.set(24)

text_area=Text(window,font=(font_name.get(),font_size.get()))
scroll_bar=Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)#manage how rows in the grid layout expands when window is resized
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N+E+S+W)
scroll_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)


frame=Frame(window)
frame.grid()
color_choser=Button(frame,text="Choose color",command=change_color)
color_choser.grid(row=0,column=0)

font_choser=OptionMenu(frame,font_name,*font.families(),command=change_font)#*font.families will return all of the varius fonts
font_choser.grid(row=0,column=1)

size_choser=Spinbox(frame,from_=10,to=90,textvariable=font_size,command=change_font)
size_choser.grid(row=0,column=2)

menubar=Menu(window)
window.config(menu=menubar)

file_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label='new',command=new_file)
file_menu.add_command(label='open',command=open_file)
file_menu.add_command(label='save',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='exit',command=exit)

edit_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Cut',command=cut)
edit_menu.add_command(label='Copy',command=copy)
edit_menu.add_command(label='Paste',command=paste)

help_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='About this program',command=about)


window.mainloop()

