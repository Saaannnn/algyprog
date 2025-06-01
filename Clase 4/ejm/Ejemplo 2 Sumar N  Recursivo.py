# Librerias a Importar
import os
from os import system

def main():
    # Variables Globales
    sum:int
    sum=0    
    # Funciones y Procedimientos
    def Sumar(x):
        nonlocal sum
        if (x>0):                           
            sum = x + Sumar (x-1)
        return sum
    
    # Programa Principal
    print("UCAB Elaborado por: Xxxxx Yyyyy")    
    print("Indique Numero entero positivo MAYOR que 1") 
    n=int(input())
    system("cls")
    suma=Sumar(n) 
    print("UCAB Elaborado por: Xxxxx Yyyyy")
    print("La SUMA de todos los numeros desde ",n," hasta 1 es: ",suma)
    
main()