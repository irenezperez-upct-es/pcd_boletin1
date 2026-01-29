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

 
