import os as os
# implementación del juego 3 en raya (mejor implementacion que juego_3_en_raya.py)

fichas= ['o','x'] 
 
def mostrar_tablero(n, movimientos_jugadores): 
 
    for i in range(n): 
        for j in range(n): 
            casilla_vacia = True 
            for k in range(len(movimientos_jugadores)): 
                movimientos_jugador= movimientos_jugadores[k] 
 
                if i in movimientos_jugador: 
                    if j in movimientos_jugador[i]: 
                        print(fichas[k],end='') 
                        casilla_vacia= False 
            if casilla_vacia: 
                print('_ ',end='') 
        print('\n') 

def movimiento_valido(n, x, y, movimientos_otro_jugador): 
    if x > n or y > n: 
        return False 
     
    if x in movimientos_otro_jugador: 
        movimientos_en_columna= movimientos_otro_jugador[x] 
        if y in movimientos_en_columna: 
            return False 
 
    return True

def jugada_ganadora(movimientos_jugador): 
    #Comprobamos si hay 3 fichas en una fila 
    for fila in movimientos_jugador: 
        movimientos_columna = movimientos_jugador[fila] 
        if len(movimientos_columna)==3: 
            return True 
    return False
 
if __name__ == "__main__": 
    #Pedimos el tamaño del tablero en que se va a realizar el juego 
    n=int(input('Introduce el tamaño del tablero cuadrado:')) 
 
    casillas_libres = n*n 
    jugador_activo = 0 
 
    movimientos_jugador_1 = {} 
    movimientos_jugador_2 = {} 
    movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2] 
 
    mostrar_tablero(n,movimientos_jugadores) 

    while casillas_libres > 0:
        casilla_jugador = input(f"JUGADOR {jugador_activo + 1}: Introduce movimiento (x, y): ")
        casilla_jugador= casilla_jugador.strip() 
        x= int(casilla_jugador.split(',')[0])-1 
        y= int(casilla_jugador.split(',')[1])-1 
 
        print(casilla_jugador,x,y) 
 
        movimientos_jugador_activo= movimientos_jugadores[jugador_activo] 
        movimientos_otro_jugador = movimientos_jugadores[(jugador_activo+1)%2] 
        if movimiento_valido(x,y, movimientos_otro_jugador): 
            mov_col= movimientos_jugador_activo.get(x,[]) 
            mov_col.append(y) 
            movimientos_jugador_activo[x]= mov_col 
 
            clear = lambda: os.system('cls') 
            clear() 
            mostrar_tablero(n, movimientos_jugadores) 
            if jugada_ganadora(movimientos_jugador_activo): 
                print(F"ENHORABUENA EL JUGADOR {jugador_activo+1} HA GANADO") 
                break 
        else: 
            frequency = 2000 # Set Frequency To 2500 Hertz 
            duration = 1000  # Set Duration To 1000 ms == 1 second 
            print('\a') 
            #winsound.Beep(frequency, duration) 
            print("Movimiento invalido. Turno para el siguiente jugador") 
 
 
        casillas_libres= casillas_libres -1 
        jugador_activo = (jugador_activo+1) % 2 
 
