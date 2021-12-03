from circulo import Circulo
from cruz import Cruz

class Cuadrado:
    def __init__(self, fila, columna, ocupado=False, jugador=0, pantalla=None):
        self.fila = fila
        self.columna = columna
        self.ocupado = ocupado
        self.jugador = jugador
        self.pantalla = pantalla
    def dibujar(self):
        forma = 0
        y = self.fila * 140 + 100
        x = self.columna * 140 + 100
        if self.jugador == 1 and self.ocupado == True:
            forma = Circulo(x, y, self.pantalla)
        elif self.jugador == 2 and self.ocupado == True:
            forma = Cruz(x, y, self.pantalla)
        if self.ocupado == True:
            return forma
    def en_blanco(self):
        if self.ocupado:
            return False
        else: 
            return True