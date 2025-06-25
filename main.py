import colorama
import numpy as np
import random as rn
from colorama import *
from numpy import *
from random import *

init(autoreset=True)
# Función para mostrar el encabezado
def encabezado():
    print(Fore.BLUE+"UCAB Elaborado por: ",end="")
    print(Fore.MAGENTA+"Jesus Blanca, Diego García, Alessandro Perez y Eleam Villalta") 
    print("  Proyecto Avance 1  ")
    print()

def generar_matrices_user(filas,columnas): #Generación de todas las células vivas al azar
    matriz = []
    for i in range(0,filas):
        fila = []
        for i in range(0,columnas):
            valor = np.random.randint(0,2)
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Función para mostrar las posiciones  con colores
def mostrar_arreglo(Matriz):
    for i in range(len(Matriz)):
        fila = ""
        for j in range(len(Matriz[i])):
            if Matriz[i][j] == 1:
                fila += Fore.LIGHTGREEN_EX + "1 "
            elif Matriz[i][j] == 0:
                fila += Fore.LIGHTRED_EX + "0 "
            elif Matriz[i][j] == 2:
                fila += Fore.LIGHTYELLOW_EX + "A "
            else:
                fila += str(Matriz[i][j]) + " "  # Por si hay otro valor diferente
        print(fila)
    print()

def aplicar_reglas_vida(matriz, i, j):
    filas, cols = np.shape(matriz)
    vecinos = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x == i and y == j) or (x < 0) or (y < 0) or (x >= filas) or (y >= cols):
                continue
            vecinos += matriz[x][y]
    if matriz[i][j] == 1:
        if (vecinos <= 1) or (vecinos >= 4):
            return 0
        else:
            return 1
    else:
        if (vecinos == 3) or (vecinos == 2):
            return 1
        else:
            return 0

def siguiente_generacion(matriz):
    filas, columnas = np.shape(matriz)
    nueva_matriz = []
    for i in range(filas):
        nueva_fila = []
        for j in range(columnas):
            nueva_fila.append(aplicar_reglas_vida(matriz, i, j))
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

def recorrido_espiral(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    recorrido = []
    top, bottom = 0, filas - 1
    left, right = 0, columnas - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            recorrido.append((top, j))
        top += 1
        for i in range(top, bottom + 1):
            recorrido.append((i, right))
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                recorrido.append((bottom, j))
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                recorrido.append((i, left))
            left += 1
    return recorrido

def recorrido_diagonal(matriz):
    recorrido = []
    filas, columnas = len(matriz), len(matriz[0])
    for s in range(columnas-2,-1,-1): 
        i = 0
        j = s
        while i < filas and j >= 0:
            recorrido.append((i, j))
            i += 1
            j -= 1
    return recorrido

def recorrido_zigzag(matriz):
    recorrido = []
    for j in range(len(matriz)):
        if j % 2 == 0:
            # Recorre de arriba a abajo
            for i in range(len(matriz[0])):
                recorrido.append((i, j))
        else:
            # Recorre de abajo a arriba
            for i in range(len(matriz[0])):
                recorrido.append((i, j))
    return recorrido

def milagro_1(matriz): 
    recorrido = recorrido_espiral(matriz)
    impares = []

    for i, j in recorrido:
        if i % 2 == 1 and j % 2 == 1:
            impares.append((i, j))

    libres = []
    for i, j in impares:
        if matriz[i][j] == 0:
            libres.append((i, j))

    if len(libres) >= int(0.5 * len(impares)) and libres:
        i, j = libres[0]  # Primera posición desocupada válida
        matriz[i][j] = 2  # Célula ángel
        print(Fore.LIGHTMAGENTA_EX+"¡Milagro 1! Nació célula ángel en la posición ({i}, {j})")
    else:
        print(Fore.LIGHTRED_EX + "Milagro 1 no ocurrió.")

    return matriz

def milagro2(matriz):
    recorrido = recorrido_diagonal(matriz)  # Nombre corregido
    nueva_matriz = matriz.copy()
    candidatos = []
    total_x_par = 0

    for i, j in recorrido:
        if i % 2 == 0:
            total_x_par += 1
            if matriz[i][j] == 0:
                candidatos.append((i, j))

    if len(candidatos) >= int(0.7 * total_x_par):
        i, j = candidatos[-1]  # última posición desocupada válida
        nueva_matriz[i][j] = 2
        print(Fore.LIGHTMAGENTA_EX+"¡Milagro 2! Nació célula ángel en {i, j}")
    else:
        print(Fore.LIGHTRED_EX+"Milagro 2 no ocurrió.")

    return nueva_matriz

def milagro3(matriz):
    nueva_matriz = matriz.copy()
    recorrido = recorrido_zigzag(matriz)
    candidatos = []
    total_y_impar = 0
    for i, j in recorrido:
        if j % 2 == 1:
            total_y_impar += 1
            if matriz[i][j] == 0:
                candidatos.append((i, j))
    if len(candidatos) >= int(0.6 * total_y_impar):
        segunda_mitad = recorrido[len(recorrido)//2:]
        for i, j in segunda_mitad:
            if (i, j) in candidatos:
                nueva_matriz[i][j] = 2  # célula ángel
                print(Fore.LIGHTBLACK_EX+"¡El milagro ocurrió! Nació célula ángel en", (i,j))
                break
    else:
        print(Fore.LIGHTRED_EX+"Milagro 3 no ocurrió.")
    return nueva_matriz

# Programa principal
def main():
    encabezado()
    # Nuevos avances, empleo de una matriz cuyas dimensiones son decididas por un input
    filas = int(input(Fore.LIGHTBLACK_EX+"Introduce la cantidad de filas de una matriz: "))
    columnas = int(input(Fore.LIGHTBLACK_EX+"Introduce la cantidad de filas de una matriz: "))
    if (filas > 20) or (columnas > 20):
        print(Fore.RED+"¡ERROR! ¡DIMENSIONES MUY GRANDES!")
    else:
        M = generar_matrices_user(filas,columnas)
        print(Fore.LIGHTBLACK_EX+"La matriz:")
        mostrar_arreglo(M)
        M2 = siguiente_generacion(M)
        print(Fore.LIGHTBLACK_EX+"Actualización:")
        mostrar_arreglo(M2)
        print(Fore.LIGHTBLACK_EX+"¿Quieres aplicar un milagro?")
        print(Fore.MAGENTA+"      1. Si")
        print(Fore.MAGENTA+"      2. No")
        Sel=int(input())
        if Sel==1:
            print(Fore.LIGHTBLACK_EX+"¿Cuál quieres aplicar?")
            print(Fore.MAGENTA+"      Milagro 1")
            print(Fore.MAGENTA+"      Milagro 2")
            print(Fore.MAGENTA+"      Milagro 3")
            Opt=int(input())
            if Opt==1:
                M3 = milagro_1(M2)
                mostrar_arreglo(M3)
            elif Opt==2:
                M3 = milagro2(M2)
                mostrar_arreglo(M3)
            elif Opt==3:
                M3 = milagro3(M2)
                mostrar_arreglo(M3)
            else:
                print(Fore.LIGHTRED_EX+"ERROR. OPCIÓN INVÁLIDA.")
        elif Sel==2:
            print(Fore.CYAN+"Fin del programa")
        else:
            print(Fore.LIGHTRED_EX+"ERROR. OPCIÓN INVÁLIDA.")

main()
