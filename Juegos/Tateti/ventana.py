from tkinter import *

color_fondo = '#f8f9fa'
color_titulos = '#212529'
color_frames = '#2a9d8f'

class Ventana:
    def __init__(self):
        self.v = Tk()
        self.v.title('Jugador')
        self.v.geometry('380x160')
        self.v.configure(bg=color_fondo)
        self.nombre_jugador = ''

        tit = Label(self.v, text='Ingrese su nombre:', bg=color_fondo, fg=color_titulos, font=('Comic Sans', 24)).pack(anchor=CENTER, padx=10, pady=5)
        self.nombre = Entry(self.v)
        self.nombre.pack(anchor=CENTER, pady=10)
        but = Button(self.v, text='OK', command=self.cerrar, bg=color_frames, fg=color_titulos).pack(anchor=CENTER)

    def cerrar(self):
        self.nombre_jugador = self.nombre.get()
        self.v.destroy()