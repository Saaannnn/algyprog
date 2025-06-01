import os
from os import system
def main():  
    # Variables Globales
    
      
    # Funciones y Procedimientos
    def Validar(x):
        if (x<0):
            bool=False
        else:
            bool=True
        return bool
    
    def Cantidad(x,co):        
        if((x//10)!=0):
            co=co+Cantidad((x//10),1)
        else:
            co=1
        return co
    
    # Programa Principal        
    # Cantidad de Dígitos de un Numero
    print("UCAB Elaborado por: Xxxxx Yyyyy")
    print("Indique número entero positivo")
    n=int(input())    
    system("cls")
    
    if(Validar(n)==False):
        print("UCAB Elaborado por: Xxxxx Yyyyy")
        print("ERROR el numero suministrado es: ",n)
        print("y debe ser entero positivo Mayor que 0")
    else:        
        # Solucion Recursiva
        cont=Cantidad(n,1)
            
        # Mostrar el Resultado
        print("UCAB Elaborado por: Xxxxx Yyyyy")
        print("La cantidad de Dígitos del número ",n," es: ",cont)
        

main() 