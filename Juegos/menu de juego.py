import os, sys,  tkinter as tk
from tkinter import *
import subprocess
from PIL import Image, ImageTk

color_fondo = '#264653'
color_titulos = '#f8f9fa'
color_frames = '#2a9d8f'
directorio = str(os.getcwd())

class Ventana():
    def __init__(self, v):
        v.title('Juegos')
        v.attributes('-fullscreen', True)
        v.configure(bg=color_fondo)

        
        tttimage = ImageTk.PhotoImage(Image.open(f'{directorio}/tateti png.png').resize((250,250)))
        pptimage = ImageTk.PhotoImage(Image.open(f'{directorio}/ppt png.png').resize((250,250)))
        
        esc = Label(v, text='Esc: Salir')
        esc.grid(row=0, column=2, padx=5, pady=20)
        esc.config(foreground=color_titulos, bg=color_fondo, font=("Comic Sans", 18))
        
        ppt = Label(v, text='Piedra Papel o Tijera')
        ppt.grid(row=4, column=1, padx=90)
        ppt.config(foreground=color_titulos, bg=color_fondo, font=("Comic Sans", 24))

        ttt = Label(v, text='TaTeTi')
        ttt.grid(row=4, column=2, padx=90)
        ttt.config(foreground=color_titulos, bg=color_fondo, font=("Comic Sans", 24))

        boton1 = Button(v, command=self.pipati, text='ppt', image=pptimage, width=250, height=250, bg=color_frames)
        boton1.image = pptimage
        boton1.grid(row=1, column=1, padx=220, pady=(150, 70), ipady=5, ipadx=5)
        
        boton2 = Button(v, command=self.tateti, text='tateti', image=tttimage, width=250, height=250, bg=color_frames)
        boton2.image = tttimage
        boton2.grid(row=1, column=2, padx=170, pady=(150, 70), ipady=5, ipadx=5)

    def tateti(self):
        subprocess.call([f'{directorio}/Tateti/tateti.py'], shell=True)

    def pipati(self):
        subprocess.call([f'{directorio}/Piedra papel o Tijera/piedrapapeltijera.py'], shell=True)


if __name__ == '__main__':
    v = Tk()
    app = Ventana(v)
    v.bind('<Escape>', lambda e: sys.exit())
    v.mainloop()