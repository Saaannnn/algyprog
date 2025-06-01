# Librerias a Importar
import os
from os import system

def main():
    # Variables Globales
    
        
    # Funciones y Procedimientos
    def Factorial(x):
        
        if (x>1):                           
            f=(x*Factorial(x-1))
        else:
            f=1
        return f 
        
        
    
    # Programa Principal
    print("UCAB Elaborado por: Xxxxx Yyyyy")    
    print("Indique Numero entero") 
    n=int(input())
    system("cls")
    if(n<0):
        print("UCAB Elaborado por: Xxxxx Yyyyy")
        print("ERROR el numero suministrado fue: ",n)
        print("y el Factorial NO esta definido para numeros NEGATIVOS")
    else:
        if(n==0)or(n==1):
            fact=1
        else:
            fact=Factorial(n) 
        
        print("UCAB Elaborado por: Xxxxx Yyyyy")
        print("El FACTORIAL del numero ",n," es: ",fact)
    
main()