import os
from os import system

def main():
    # Variables Globales
    r:int
    r=0
    # Funciones y Procedimientos
    def recursive_function(num):
        nonlocal r
        if (num<6):
            
            if(num<5):
                print(num,end=",")
            else:
                print(num,end=".")
                
            r=recursive_function(num+1)
        return r
    def recursive_function1(num):
        nonlocal r
        if (num<6):
            r=recursive_function1(num+1)
            if(num>1):
                print(num,end=",")
            else:
                print(num,end=".")
                
            #r=recursive_function(num+1)
        return r
            
    print("UCAB Elaborado por: Xxxxx Yyyyy ")
    print("Los Números en forma Progresiva del 1 al 5 son: ")
    recursive_function(1)
    print()
    print("Los Números en forma Regresiva del 5 al 1 son: ")
    recursive_function1(1)
    print()    
    
main()