import os
from os import system

def main():
    # Variables Globales
    n1:int
    n2:int
    cont:int
    cont=0
    prod:int
    
    # Funciones y Procedimientos
    def Validar(x):
        if (x<0):
            bool=False
        else:
            bool=True
        return bool
    
    def Producto(ma,co):        
        if(co<men):
            s=(ma+Producto(ma,co+1))
        else:
            s=0
        return s
    
    # Programa Principal        
    # Producto por el Metodo de Sumas Sucesivas
    print("UCAB Elaborado por: Xxxxx Yyyyy")
    print("Indique número 1 entero positivo Mayor que cero")
    n1=int(input()) 
    print("Indique número 2 entero positivo Mayor que cero")
    n2=int(input())
    system("cls")
    
    if(Validar(n1)==False)or (Validar(n2)==False):
        print("UCAB Elaborado por: Xxxxx Yyyyy")
        print("ERROR los numeros suministrados son: ",n1," y ",n2)
        print("y AMBOS deben ser enteros positivos Mayores que 0")
    else:
        # Buscar el Mayor para hacer más eficiente el cálculo
        if(n1>=n2):
            may=n1
            men=n2
        else:
            may=n2
            men=n1                  
        
            
        # Solucion Recursiva
        prod=Producto(may,0)
            
        # Mostrar el Resultado
        print("UCAB Elaborado por: Xxxxx Yyyyy")
        print("El Producto del número ",n1," por ",n2)
        print("a través del Método de Sumas Sucesivas es: ",prod) 

main() 