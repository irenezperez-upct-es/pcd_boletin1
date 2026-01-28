# funcion para mostrar el tablero por pantalla con una dimensión n y asumiendo que los jugadores han realizado movimientos (movimientos_jugadores)
import pytest
import os as os



fichas= ['o','x'] 
def generar_tablero(n, movimientos_jugadores): 
    # n es el tamaño del tablero (n x n)
    # movimientos_jugadores: lista con los movimientos de cada jugador
    tablero=[] 
    for i in range(n): # iteramos por las filas
        fila=['_' for i in range(n)] # inicializamos la fila con casillas vacías
        for j in range(n): # iteramos por las columnas
            casilla_vacia = True # asumimos que la casilla está vacía
            for k in range(len(movimientos_jugadores)): # iteramos por los jugadores
                movimientos_jugador= movimientos_jugadores[k] # dict con los movimientos del jugador k
 
                if i in movimientos_jugador: # si el jugador k ha jugado en la fila i
                    if j in movimientos_jugador[i]: # si el jugador k ha jugado en la columna j
                        fila[j]=fichas[k] # asignamos la ficha del jugador k a la casilla
        tablero.append(fila) # añadimos la fila al tablero
    return tablero 
    

n = 3
#t= generar_tablero(n, movimientos_jugadores) 
#print(t, len(t))

# PASO 2
# Desarrollar un método que permita determinar si el movimiento de un jugador es válido o no

""" 
Método que comprueba que un movimiento de un jugador es válido 
    * x: fila donde el jugador quiere colocar la ficha. 
    * y: columna donde el jugador quiere colocar su ficha. 
    * movimientos_otro_jugador: listado con las celdas ocupadas por el otro 
jugador. 
""" 
def movimiento_valido(x, y, movimientos_otro_jugador): 
    if x > n or y > n: # si la casilla (fila o columna) donde se quiere poner la ficha es mayor que el tamaño del tablero:
        return False # el movimiento no es válido
    # comprobamos si el otro jugador ya ha puesto una ficha en esa fila y columna
    if x in movimientos_otro_jugador:   # si la fila x está en los movimientos del otro jugador
        movimientos_en_columna= movimientos_otro_jugador[x] # obtenemos las columnas donde el otro jugador ha jugado en la fila x
        if y in movimientos_en_columna: # si la columna y está en las columnas donde el otro jugador ha jugado en la fila x
            return False # entonces el movimiento no es válido
    return True 


# PASO 3
# método que permite determinar si un nuevo movimiento de un jugador le permite ganar el juego
def jugada_ganadora(movimientos_jugador): 
    # FUNCIÓN MODOFICADA PARA PODER SACAR TODAS LAS JUGADAS GANADORAS
    """ 
    Método que permite determinar si los movimientos de un jugador le 
    permite ganar una partida. 
    Parámetros: 
    * movimientos_jugador: dict con el conjunto de movimientos de un 
    jugador 
    dentro del diccionario la clave es la fil (x) y el valor es una lista con las columnas (y) 
        donde ese jugador ha puesto ficha
    """ 
    #Comprobamos si hay 3 fichas en una fila
    """for fila in movimientos_jugador: # recorremos cada fila donde el jugador ha jugado
        movimientos_columna = movimientos_jugador[fila] # obtebemos la lusra de columnas ocupadas en esa fila
        if len(movimientos_columna)==3: 
            return True 
        
    return False"""

    tablero_ganador = [[0 for i in range(n)] for j in range(n)] # inicializamos una matriz n x n con ceros
    
    for fila in movimientos_jugador: # recorremos cada fila donde el jugador ha jugado
        movimientos_columna = movimientos_jugador[fila] # obtebemos la lusra de columnas ocupadas en esa fila
        for columna in movimientos_columna:
            tablero_ganador[fila -1][columna -1] = 1 # marcamos la posición en el tablero ganador
    
    # comprobamos filas
    for i in range(n):
        if sum(tablero_ganador[i]) == 3: # comprobamos filas
            return True

    # comprobamos columnas
    for j in range(n):
        if sum(tablero_ganador[i][j] for i in range(n)) == 3: # comprobamos columnas
            return True
    
    # comprobamos diagonal 
    if sum(tablero_ganador[i][i] for i in range(n)) == 3: # diagonal principal
        return True
        
    return False
        

# PASO 4
# añadimos la lógica del juego que permite hacerlo interactivo
# Primero implementamos el método que permita mostrar el estado actual del tablero por pantalla:
def mostrar_tablero(tablero): 
    """  
    Método que muestra el estado actual del tablero 
     
    Parámetros: 
        * tablero: dict con el tablero a mostrar 
    """ 
    for fila in tablero: 
        # cada fiña es una lista, ej: ['X','_','O']
        for celda in fila: # para cada celda de la fila
            # cada celda es un caracter X, O, _   
            print(celda,end='') # imprime la celsa sin salto de línea
        print('\n') 

# implementamos el bucle que permite a cada uno de los dos jugadores ir añadiendo movimientos:

# INICIO DEL JUEGO
#Pedimos el tamaño del tablero en que se va a realizar el juego 
n=int(input('Introduce el tamaño del tablero cuadrado:')) 
 
casillas_libres = n*n # cuantas casillas hay en total
jugador_activo = 0 # indica que jugador está activo (0 o 1)
movimientos_jugador_1 = {} 
movimientos_jugador_2 = {} 
movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2] 
 
tablero= generar_tablero(n,movimientos_jugadores) # se genera el tablero (inicialmente vacio)
mostrar_tablero(tablero) 
 
while casillas_libres > 0: # el juego dura mientras haya casillas libres
    # si se llenan todas, termina en empate
 
    casilla_jugador = input(f"JUGADOR {jugador_activo+1}: Introduce movimiento (x,y): ") # se pide al jugador activo que introduzca su movimiento
     
    casilla_jugador= casilla_jugador.strip() # eliminamos los espacios en blanci al principio y al final
    # ahora dividimos la entrada por la coma. restamos uno porque el usuario lo mete desde 1 pero python usa índices
    x= int(casilla_jugador.split(',')[0])-1   # lo que hay antes de la coma es la fila
    y= int(casilla_jugador.split(',')[1])-1   # lo que hay después de la coma es la columna
 
    print(casilla_jugador,x,y) # muestra la casilla introducida y los índices correspondientes
 
    movimientos_jugador_activo= movimientos_jugadores[jugador_activo] # selecciona el dict del jugador que está jugando
    movimientos_otro_jugador = movimientos_jugadores[(jugador_activo+1)%2] # selecciona el dict del otro jugador. (jugador_activo+1)%2 hace que alterne entre 0 y 1
    if movimiento_valido(x,y, movimientos_otro_jugador): # comprueba si el movimiento es válido
        mov_col= movimientos_jugador_activo.get(x,[]) # obtiene la lista de colunnas ocupadas en la fila x. Si no existe la fila x, devuelve una lista vacía
        mov_col.append(y) # añade la nueva columna y a la lista de columnas ocupadas en la fila x
        movimientos_jugador_activo[x]= mov_col # actualiza el dict del jugador activo
 
        clear = lambda: os.system('cls') # limpia la pantalla en windows
        clear() 
        tablero= generar_tablero(n,movimientos_jugadores) # genera tablero actualizado
        mostrar_tablero(tablero) 
        if jugada_ganadora(movimientos_jugador_activo): # si el jugador tiene una jugada ganadora
            print(F"ENHORABUENA EL JUGADOR {jugador_activo+1} HA GANADO") 
            break # termina el juego
    else: 
        # frequency y duration es para emitir el sonido en windows
        frequency = 2000 # Set Frequency To 2500 Hertz 
        duration = 1000  # Set Duration To 1000 ms == 1 second 
        print('\a') # el movimiento es inválido, emite un sonido
        print("Movimiento invalido. Turno para el siguiente jugador") 
 
    casillas_libres= casillas_libres -1 # una casilla menos disponible
    jugador_activo = (jugador_activo+1) % 2 # se cambia el jugador activo


# PARA EJERCICIO OPCIONAL: guardar las posiciones en una matriz 3x3 paar que sea más limpio
