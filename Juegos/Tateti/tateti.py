#tateti
import sys, pygame as pg
from tkinter import *
from ventana import Ventana
from tablero import Tablero

app = Ventana()
app.v.bind('<Escape>', lambda e: sys.exit())
app.v.mainloop()

pg.init()
pg.font.init()

pantalla = pg.display.set_mode((480, 480))
pg.display.set_caption('TaTeTi')
fuente = pg.font.SysFont('Arial', 24)

tab = Tablero(pantalla)
faltab = Tablero(pantalla)

ttt = True
while ttt:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            ttt = False
    pantalla.fill((57, 62, 70))
    tab.dibujar_lineas()
    cont = fuente.render(f'{app.nombre_jugador}: {tab.j1}   CPU: {tab.ia}', True, (238, 238, 238))
    rein = fuente.render('tab: reiniciar', True, (238, 238, 238))
    pantalla.blit(cont, (150, 0))
    pantalla.blit(rein, (30, 452))

    if tab.game_over and tab.f:
        tab.check_ganador(True)
        tab.f = False
    
    tab.jug_mov(faltab)
    tab.dibujar_cuadrados()
    tab.ia_move(faltab)
    tab.check_ganador(False)

    if event.type == pg.KEYDOWN:
	    if event.key == pg.K_TAB:
		    tab.resetear()
		    faltab.resetear()
    
    pg.display.update()
pg.quit()