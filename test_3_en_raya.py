# implementación de los test unitaros para el juego 3 en raya

from juego_3_en_raya import generar_tablero, movimiento_valido, jugada_ganadora    
import os as os

# testeamos que el tablero se genera correctamente con las dimensiones adecuadas 
def test_generar_tablero():  

    mov_jugador_1 = {}   

    mov_jugador_2 = {}   

    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]   

    n=3  

    t= generar_tablero(n, movimientos_jugadores)

    assert len(t)== n  

    for f in t:  
        assert len(f) == n 

# testeamos si un movimiento es válido mendiante la función movimiento_valido
def test_movimiento_columna_fuera_tablero():
    n = 3 
    movimientos_otro_jugador={} 
    x=  1 
    y=  n+1 
    assert False == movimiento_valido(x,y,movimientos_otro_jugador) 

def test_movimiento_fila_y_columna_fuera_tablero(): 
    n = 3
    movimientos_otro_jugador={} 
    x=  n+1 
    y=  n+1 
    assert False == movimiento_valido(x,y,movimientos_otro_jugador) 
 
def test_movimiento_incorrecto(): 
    movimientos_otro_jugador={2:[3]} 
    x=  2 
    y=  3 
    assert False == movimiento_valido(x,y,movimientos_otro_jugador)

# testeamos si una jugada es ganadora mediante la función jugada_ganadora
def test_no_ganador_falta_casilla(): 
    movimientos_jugador={2:[2,3]} 
    assert False == jugada_ganadora(movimientos_jugador) 

def test_no_ganador_movimientos():
    # movimientos dispersos que no forman la línea
    movimientos_jugador = {
        1: [1],
        2: [3],
        3: [2]
    }
    assert False == jugada_ganadora(movimientos_jugador) 
 
def test_ganador_fila(): 
    # el jugador ocupa toda la fila 2
    movimientos_jugador={2:[1,2,3]} # creamos diccionario que representa los movimientos del jugador
    assert True == jugada_ganadora(movimientos_jugador) # esta línea comprueba que la funcion devuelve True porque el jugador tiene 3 fichas en la misma fila

def test_ganador_columna():
    # el jugador ocupa la columna 1 en las filas 1, 2, 3
    movimientos_jugador = {
        1: [1],
        2: [1],
        3: [1]
    }
    assert True == jugada_ganadora(movimientos_jugador)

def test_ganador_diagonal():
    # el jugador ocupa (1,1), (2,2), (3,3)
    movimientos_jugador = {
        1: [1],
        2: [2],
        3: [3]
    }
    assert True == jugada_ganadora(movimientos_jugador)