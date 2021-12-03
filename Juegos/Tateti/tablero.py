import pygame as pg
from cuadrado import Cuadrado
from random import choice


color_p1 = 17, 153, 158
color_p2 = 240, 84, 84

class Tablero():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.jugador = 1
        self.game_over = False
        self.f = True
        self.t_cuadrado = 140
        self.j1 = 0
        self.ia = 0
        self.c1 = Cuadrado(0, 0, pantalla=self.pantalla)
        self.c2 = Cuadrado(0, 1, pantalla=self.pantalla)
        self.c3 = Cuadrado(0, 2, pantalla=self.pantalla)
        self.c4 = Cuadrado(1, 0, pantalla=self.pantalla)
        self.c5 = Cuadrado(1, 1, pantalla=self.pantalla)
        self.c6 = Cuadrado(1, 2, pantalla=self.pantalla)
        self.c7 = Cuadrado(2, 0, pantalla=self.pantalla)
        self.c8 = Cuadrado(2, 1, pantalla=self.pantalla)
        self.c9 = Cuadrado(2, 2, pantalla=self.pantalla)
        self.cuadrados = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9]
        for i in self.cuadrados:
            i.dibujar()

    def buscar_cuadrado(self, fila, columna):
        if fila == 0:
            if columna == 0:
                return self.c1
            elif columna == 1:
                return self.c2
            elif columna == 2:
                return self.c3
        elif fila == 1:
            if columna == 0:
                return self.c4
            elif columna == 1:
                return self.c5
            if columna == 2:
                return self.c6
        elif fila == 2:
            if columna == 0:
                return self.c7
            elif columna == 1:
                return self.c8
            elif columna == 2:
                return self.c9
    
    def dibujar_cuadrados(self):
        for i in self.cuadrados:
            i.dibujar()
    
    def cuadrados_libres(self):
        libres = 0
        for i in self.cuadrados:
            if i.en_blanco():
                libres += 1
        return libres

    def get_cl(self):
        lib = []
        for i in self.cuadrados:
            if not i.ocupado:
                lib.append(i)
        return lib

    def dibujar_lineas(self):
        pg.draw.line(self.pantalla, (238, 238, 238), (30, 170), (450, 170)),
        pg.draw.line(self.pantalla, (238, 238, 238), (30, 310), (450, 310)),
        pg.draw.line(self.pantalla, (238, 238, 238), (170, 30), (170, 450)),
        pg.draw.line(self.pantalla, (238, 238, 238), (310, 30), (310, 450))
    def dibujar_linea_vertical(self, x, jugador):
        if jugador == 1:
            color = color_p1
        else: color = color_p2
        if self.game_over:
            pg.draw.line(self.pantalla, color, (x * 130 + 100, 50), (x * 130 + 100, 430), 4)
    def dibujar_linea_horizontal(self, y, jugador):
        if jugador == 1:
            color = color_p1
        else: color = color_p2
        if self.game_over:
            pg.draw.line(self.pantalla, color, (40, y * 140 + 100), (440, y * 140 + 100), 4)
    def dibujar_linea_diagonal_a(self, jugador):
        if jugador == 1:
            color = color_p1
        else: color = color_p2
        if self.game_over:
            pg.draw.line(self.pantalla, color, (50, 430), (430, 50), 4)
    def dibujar_linea_diagonal_b(self, jugador):
        if jugador == 1:
            color = color_p1
        else: color = color_p2
        if self.game_over:
            pg.draw.line(self.pantalla, color, (50, 50), (430, 430), 4)
    
    def contador(self, p):
        if p == 1:
            self.j1 += 1
        if p == 2:
            self.ia += 1
    
    def resetear(self):
        self.game_over = False
        self.jugador = 1
        self.f = True
        self.pantalla.fill((57, 62, 70))
        self.dibujar_lineas()
        for i in self.cuadrados:
            i.ocupado = False
            i.jugador = 0
            self.dibujar_cuadrados()

    def empate(self):
        if self.completo() == True and self.check_ganador() == 0:
            return True
        else: 
            return False

    def check_ganador(self, su):
        if self.c1.jugador == self.c4.jugador and self.c7.jugador == self.c4.jugador and self.c1.jugador != 0:
            if su:
                self.game_over = True
            self.dibujar_linea_vertical(0, self.c1.jugador)
            if self.game_over and su:
                self.contador(self.c1.jugador)
            ganador = self.c1.jugador
            return ganador
        
        elif self.c2.jugador ==  self.c5.jugador and self.c8.jugador == self.c5.jugador and self.c2.jugador != 0:
            if su:
                self.game_over = True
            self.dibujar_linea_vertical(1, self.c2.jugador)
            if self.game_over and su:
                self.contador(self.c2.jugador)
            ganador = self.c2.jugador
            return ganador
        
        elif self.c3.jugador == self.c6.jugador and self.c9.jugador == self.c6.jugador and self.c3.jugador != 0:
            if su:
                self.game_over = True
            self.dibujar_linea_vertical(2, self.c3.jugador)
            if self.game_over and su:
                self.contador(self.c3.jugador)
            ganador = self.c3.jugador
            return ganador
        
        elif self.c1.jugador == self.c2.jugador and self.c3.jugador == self.c2.jugador and self.c1.jugador != 0:
            if su:
                self.game_over = True
            self.dibujar_linea_horizontal(0, self.c1.jugador)
            if self.game_over and su:
                self.contador(self.c1.jugador)
            ganador = self.c1.jugador
            return ganador
        
        elif self.c4.jugador == self.c5.jugador and self.c6.jugador == self.c5.jugador and self.c4.jugador != 0:
            if su:
                self.game_over = True
            self.dibujar_linea_horizontal(1, self.c4.jugador)
            if self.game_over and su:
                self.contador(self.c4.jugador)
            ganador = self.c4.jugador
            return ganador
        
        elif self.c7.jugador == self.c8.jugador and self.c9.jugador == self.c8.jugador and self.c7.jugador != 0:
            if su:
                self.game_over = True
            self.dibujar_linea_horizontal(2, self.c7.jugador)
            if self.game_over and su:
                self.contador(self.c7.jugador)
            ganador = self.c7.jugador
            return ganador
        
        elif self.c1.jugador == self.c5.jugador and self.c9.jugador == self.c5.jugador and self.c1.jugador != 0:
            if su:
                self.game_over = True
            self.dibujar_linea_diagonal_b(self.c1.jugador)
            if self.game_over and su:
                self.contador(self.c1.jugador)
            ganador = self.c1.jugador
            return ganador
        
        elif self.c7.jugador == self.c5.jugador and self.c3.jugador == self.c5.jugador and self.c7.jugador != 0:
            if su:
                self.game_over = True
            self.dibujar_linea_diagonal_a(self.c7.jugador)
            if self.game_over and su:
                self.contador(self.c7.jugador)
            ganador = self.c7.jugador
            return ganador
        else:
            return 0

    def marcar_cuadrado(self, fila, columna, jugador):
        if fila == 0:
            if columna == 0:
                self.c1.ocupado = True
                self.c1.jugador = jugador
            elif columna == 1:
                self.c2.ocupado = True
                self.c2.jugador = jugador
            elif columna == 2:
                self.c3.ocupado = True
                self.c3.jugador = jugador
        elif fila == 1:
            if columna == 0:
                self.c4.ocupado = True
                self.c4.jugador = jugador
            elif columna == 1:
                self.c5.ocupado = True
                self.c5.jugador = jugador
            if columna == 2:
                self.c6.ocupado = True
                self.c6.jugador = jugador
        elif fila == 2:
            if columna == 0:
                self.c7.ocupado = True
                self.c7.jugador = jugador
            elif columna == 1:
                self.c8.ocupado = True
                self.c8.jugador = jugador
            elif columna == 2:
                self.c9.ocupado = True
                self.c9.jugador = jugador
    
    def minimax(self):   
        opciones = self.get_cl()
        c = 0
        gana, pierde = False, False
        score = 0

        if not gana: 
            for c in range(len(opciones)):
                cuad = opciones[c]
                if cuad.en_blanco():
                    cuad.jugador = 2
                    cuad.ocupado = True
                    if self.check_ganador(False) == 2:
                        gana = True
                        score = 10
                        cuad.jugador = 0
                        cuad.ocupado = False
                        break
                    cuad.jugador = 0
                    cuad.ocupado = False
        if not gana and not pierde:    
            for c in range(len(opciones)):
                cuad = opciones[c]
                if cuad.en_blanco():
                    cuad.jugador = 1
                    cuad.ocupado = True
                    if self.check_ganador(False) == 1:
                        cuad.jugador = 2
                        score = 5
                        pierde = True
                        cuad.jugador = 0
                        cuad.ocupado = False
                        break
                    else:
                        c = choice([x for x in range(len(opciones)-1)])
                        score = 1                
                    cuad.jugador = 0
                    cuad.ocupado = False
        return c, score

    def completo(self):
        for i in self.cuadrados:
            c = False if not i.ocupado else True
        return c

    def jug_mov(self, faltab):
        if self.jugador == 1:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and not self.game_over:

                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    fila_click = int(mouseY // self.t_cuadrado)
                    columna_click = int(mouseX // self.t_cuadrado)

                    if self.buscar_cuadrado(fila_click, columna_click).en_blanco() == True:
                        self.marcar_cuadrado(fila_click, columna_click, 1)
                        faltab.marcar_cuadrado(fila_click, columna_click, 1)
                        self.dibujar_cuadrados()
                        if self.check_ganador(False):
                            self.game_over = True
                        self.jugador = self.jugador % 2 + 1
                    return fila_click, columna_click

    def ia_move(self, faltab):
        opciones = faltab.get_cl()
        if self.jugador == 2 and not self.game_over:
            bestMove = Cuadrado(0, 0)
            bestc, score = self.minimax()
            if len(opciones) < 2 and bestc == 0:
                print('tablero completo')
            else:
                bestMove = opciones[bestc]
            if score != 0:        
                if self.buscar_cuadrado(bestMove.fila, bestMove.columna).en_blanco() == True:
                    self.marcar_cuadrado(bestMove.fila, bestMove.columna, 2)
                    faltab.marcar_cuadrado(bestMove.fila, bestMove.columna, 2)
                    if self.check_ganador(False):
                        self.game_over = True
            self.dibujar_cuadrados()
            self.jugador = self.jugador % 2 + 1
            return bestMove.fila, bestMove.columna
