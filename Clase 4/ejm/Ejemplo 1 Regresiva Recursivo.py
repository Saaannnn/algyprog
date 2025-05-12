# Librerias a Importar
import os
from os import system

def main():
    # Funciones y Procedimientos
    def Regresiva(x):
        if (x>0):
            if(x>1):
                print(x,end=", ")
            else:
                print(x,end=".")
                
            return Regresiva (x-1)
    
    # Programa Principal
    print("UCAB Elaborado por: Xxxxx Yyyyy")    
    print("Indique Numero entero positivo MAYOR que 1") 
    n=int(input())
    system("cls") 
    print("UCAB Elaborado por:Xxxxx Yyyyy")
    print("Los numeros en forma regresiva desde ",n," son:")
    Regresiva(n)
    print()    
main()