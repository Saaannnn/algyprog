# Librerias a importar
import time
import numpy as np
import random
import os
from os import system 

def main():
    # Declarar e inicializar Estructuras
    n=np.array([0]*2000000)
    
    
    # Programa Principal
    # Generar un Arreglo Ordenado Ascendentemente
    
    for i in range(0,len(n)-1,1):
        n[i]=i      
    
    
    print("UCAB Elaborado por Rodolfo Holguin")
    print("Indique un numero a buscar en el arreglo")
    num=int(input())
    # Opcion 1 Busqueda Secuencial Elemental
    z=0
    star=time.time()
    for i in range(0,len(n)-1,1):
        if(num==n[i]):
            z=1
            print("El numero ",num," esta en el Arreglo")
            print("en la posicion ",i)            
            break
        
    if(z==0):
        print("El numero ",num," NO esta en el Arreglo")
    stop=time.time()
    t=(stop-star)
    print("Busqueda Secuencial Elemental")
    print("El Tiempo de Ejecucion fue de: ",t," microsegundos")
    
    # Opcion 2 Busqueda Binaria   
    
    z=0    
    star=time.time()  
    
   # Busqueda Binaria
    inicio=0
    fin=len(n)-1
    mitad=0
    while(inicio<=fin):
        mitad=((inicio +fin )//2)
        if(n[mitad] < num):
            inicio = (mitad+1)
        elif(n[mitad] > num):
            fin = (mitad-1)
        else:
            z=1
            print("El numero ",num," esta en el Arreglo")
            print("en la posicion ",mitad)            
            break
        
    if(z==0):
        print("El numero ",num," NO esta en el Arreglo")
    stop=time.time()
    t=(stop-star)
    print("Busqueda Binaria")
    print("El Tiempo de Ejecucion fue de: ",t," microsegundos")
main()
