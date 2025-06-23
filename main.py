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
    for i in range(0,filas,1):
        fila = []
        for i in range(0,columnas,1):
            valor = np.random.randint(0,2)
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Función para mostrar las posiciones  con colores
def mostrar_arreglos(M, titulo=""):
    if titulo:
        print(f"\n{titulo}")
    # Mostrar la matriz
    posiciones = []
    for i in range (len(M)):
        for j in range (len(M)):
            if M[i][j]==1:
                posiciones.append((i,j)) #Creación de una lista con todas las posiciones vivas
            
        print(Fore.LIGHTGREEN_EX + str(posiciones) + Style.RESET_ALL)
    return posiciones

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
# Programa principal
def main():
    encabezado()
    # Nuevos avances, empleo de una matriz cuyas dimensiones son decididas por un input
    filas = int(input("Introduce la cantidad de filas de una matriz: "))
    columnas = int(input("Introduce la cantidad de filas de una matriz: "))
    if (filas > 20) or (columnas > 20):
        print(Fore.RED+"¡ERROR! ¡DIMENSIONES MUY GRANDES!")
    else:
        M = generar_matrices_user(filas,columnas)
        print("Posiciones con vida en la matriz: ")
        mostrar_arreglos(M)
        M2 = reglas_de_la_vida(M)
        print("Posiciones con vida después de una generación: ")
        mostrar_arreglos(M2)
main()
