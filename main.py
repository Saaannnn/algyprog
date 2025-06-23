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

def contar_vecinos(matriz,x,y):
    # Cuenta cuantas celulas vivas (Representadas con el número uno) hay alrededor de la celda (x,y), (fila,columna). considerando los bordes como celulas vacias.
    vecinos = 0
    filas,columnas = matriz.shape
    # Desplazamiento en filas y columnas
    desplazamiento = [-1, 0, 1] 
    # Recorrer las posiciones vecinas (inclyendo diagonales)
    for dx in desplazamiento: # Desplazamiento en filas
        for dy in desplazamiento: # Desplazamiento en columnas
            if dx == 0 and dy == 0:
                continue # Saltar la celda central (x,y)
            else:
                nx = x + dx # Fila vecina
                ny = y + dy # Columna vecina
                # Verificar si la posicion esta dentro de los limites
                if 0 <= nx < filas and 0 <= ny < columnas:
                    if matriz[nx][ny] == 1:
                        vecinos += 1
    return vecinos 

def reglas_de_la_vida(matriz):
    matriz=np.array(matriz)
    filas,columnas = matriz.shape
    nueva_matriz = np.zeros((filas,columnas), dtype=int)    
    for i in range(filas):
        for j in range(columnas):
            vivos = contar_vecinos(matriz,i,j)
            if matriz[i,j] == 1:
                # Regla 1: muerte por soledad
                if vivos <= 1:
                    nueva_matriz[i,j]=0
                # Regla 2: muerte por sobrepoblación
                elif vivos >= 4:
                    nueva_matriz[i,j]=0
                # Regla 3: supervivencia de la célula
                elif 2 <= vivos <= 3:
                    nueva_matriz[i,j]=1
            else:
                # Regla 4: Nacimiento
                if vivos == 3:
                    nueva_matriz[i,j]=1
                else:
                    nueva_matriz[i,j]=0
    return nueva_matriz.tolist()

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
