# Librerias a Importar
import random
import numpy as np

def main():
    li=np.array([20,27,12,30,18,22,26])
    le=np.array([0]*7)
    # le=np.full(7,0)
    # Definir Variables Globales
    
    # Funciones y Procedimientos
    def Encabezado(x):
        print("UCAB Elaborado por: ",x)

    def Totalgol(li):
        sum=0
        for i in range(0,len(li),1):
            sum +=li[i]
        return sum

    def Ordenarasc(x):
        for i in range(0,len(x)-1,1):
            for j in range(i+1,len(x),1):
                if(x[j]<x[i]):
                    aux=x[i]
                    x[i]=x[j]
                    x[j]=aux 
       

    
    # Programa Principal
    for i in range(0,len(le),1):
        y=random.randint(10,27)
        le[i]=y

    # Encabezado
    Encabezado("Xxxxxx Yyyyyyy")
    # Entrada de Datos
    print("Los Goles de la Liga Italiana son: ")
    for i in range(0,len(li),1):
        print(li[i],end=" ")
    print()
    print("Los Goles de la Liga Espanola son: ")
    for i in range(0,len(le),1):
        print(le[i],end=" ")
    print()
    # Procesamiento de Datos
    sumli=Totalgol(li)
    print("El total de Goles de la Liga Italiana es: ",sumli)
    sumle=Totalgol(le)
    print("El total de Goles de la Liga Española es: ",sumle)
    Ordenarasc(li)
    print("El arreglo de goles de la liga italiana ordenedo es: ")
    for i in range(0,len(li),1):
        print(li[i],end=" ")
    print()
    Ordenarasc(le)
    print("El arreglo de goles de la liga española ordenedo es: ")
    for i in range(0,len(le),1):
        print(le[i],end=" ")
    print()
    # Salida de Datos   
    
main()