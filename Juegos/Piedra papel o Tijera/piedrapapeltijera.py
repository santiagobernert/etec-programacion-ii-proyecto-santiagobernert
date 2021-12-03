import numpy as np, cv2, sys
from tkinter import *
from keras.models import load_model
from random import choice

fuente = cv2.FONT_HERSHEY_COMPLEX

cam = cv2.VideoCapture(0)
cam.set(3, 1920)
cam.set(4, 1080)

modelo = load_model('modelo-piedra-papel-o-tijera.h5')

color_fondo = '#f8f9fa'
color_titulos = '#212529'
color_frames = '#2a9d8f'
color_texto_ocv = 255, 255, 255

PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERA = 'tijera'

nombre_jugador = ''

mov_jug = {0: 'piedra',
           1: 'papel',
           2: 'papel',
           3: 'nada'}

img_cpu = {'piedra': 'C:/Users/Profesores/Downloads/piedra.jpg',
           'papel': 'C:/Users/Profesores/Downloads/papel.png',
           'tijera': 'C:/Users/Profesores/Downloads/tijeras.png',
           'nada': 'C:/Users/Profesores/Downloads/nada.png'}
class Ventana:
    def __init__(self, v):
        v.title('Jugador')
        v.geometry('380x160')
        v.configure(bg=color_fondo)

        tit = Label(v, text='Ingrese su nombre:', bg=color_fondo, fg=color_titulos, font=('Comic Sans', 24)).pack(anchor=CENTER, padx=10)
        self.nombre = Entry(v)
        self.nombre.pack(anchor=CENTER)
        but = Button(v, text='OK', command=self.cerrar, bg=color_frames, fg=color_titulos).pack(anchor=CENTER)

    def cerrar(self):
        global nombre_jugador
        nombre_jugador = self.nombre.get()
        v.destroy()


v = Tk()
app = Ventana(v)
v.bind('<Escape>', lambda e: sys.exit())
v.mainloop()

class PiedraPapelTijera():
    def __init__(self):
        self.jugador = 0
        self.cpu = 0
        self.empates = 0
        self.mov_jugador = 0
        self.mov_cpu = 0
        self.jugadas = 0
    
    def calcular_ganador(self):
        if self.mov_jugador == self.mov_cpu:
            self.empates += 1
            self.jugadas += 1
            return 'empate'
        if self.mov_jugador == PIEDRA and self.mov_cpu == TIJERA:
            self.jugador += 1
            self.jugadas += 1
            return nombre_jugador
        elif self.mov_jugador == PAPEL and self.mov_cpu == PIEDRA:
            self.jugador += 1
            self.jugadas += 1
            return nombre_jugador
        elif self.mov_jugador == TIJERA and self.mov_cpu == PAPEL:
            self.jugador += 1
            self.jugadas += 1
            return nombre_jugador
        elif self.mov_cpu == PIEDRA and self.mov_jugador == TIJERA:
            self.cpu += 1
            self.jugadas += 1
            return 'cpu'
        elif self.mov_cpu == PAPEL and self.mov_jugador == PIEDRA:
            self.cpu += 1
            self.jugadas += 1
            return 'cpu'
        elif self.mov_cpu == TIJERA and self.mov_jugador == PAPEL:
            self.cpu += 1
            self.jugadas += 1
            return 'cpu'
        else:
            return 'no hay movimiento'
    
    def cpu_elige(self):
        x = choice([PIEDRA, PAPEL, TIJERA])
        return x

mov = 'nada'
ppt = True
juego = PiedraPapelTijera()
while ppt:
    ret, frame = cam.read()
    if not ret:
        continue
    
    cv2.rectangle(frame, (0, 0), (1300, 150), (255, 105, 105), -1)
    cv2.rectangle(frame, (0, 0), (150, 800), (255, 105, 105), -1)
    cv2.rectangle(frame, (450, 0), (1300, 800), (255, 105, 105), -1)
    cv2.rectangle(frame, (150, 450), (450, 800), (255, 105, 105), -1)

    cv2.rectangle(frame, (150, 150), (450, 450), (255, 255, 255), 2)
    cv2.rectangle(frame, (850, 150), (1150, 450), (255, 255, 255), 2)

    img = frame[150:450, 150:450]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (300, 300))

    pred = modelo.predict(np.array([img]).reshape(-1, 300, 300, 1))
    num = np.argmax(pred[0])
    juego.mov_jugador = mov_jug[num]
    
    juego.mov_cpu = mov
    if cv2.waitKey(10) == ord('p'):
        mov = juego.cpu_elige()
        juego.calcular_ganador()

    frame[150:450, 850:1150] = cv2.imread(img_cpu[juego.mov_cpu])

    if cv2.waitKey(30) == ord('q'):
        break

    cv2.putText(frame, f'{nombre_jugador}: {juego.jugador}', (150, 90), fuente, 1.2, color_texto_ocv, 2, cv2.LINE_AA)
    cv2.putText(frame, f'CPU: {juego.cpu}', (850, 90), fuente, 1.2, color_texto_ocv, 2, cv2.LINE_AA)
    cv2.putText(frame, f'{nombre_jugador} juega: {juego.mov_jugador}', (130, 110), fuente, 1.2, color_texto_ocv, 2, cv2.LINE_AA)
    cv2.putText(frame, f'CPU juega: {mov}', (835, 500), fuente, 1.2, color_texto_ocv, 2, cv2.LINE_AA)
    cv2.putText(frame, f'Ganador: {juego.calcular_ganador()}', (400, 620), fuente, 1.2, color_texto_ocv, 2, cv2.LINE_AA)

    cv2.namedWindow('Piedra Papel o Tijera', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Piedra Papel o Tijera', 1340, 720)
    cv2.imshow('Piedra Papel o Tijera', frame)
            
cam.release()
cv2.destroyAllWindows()