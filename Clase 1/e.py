import numpy
import numpy as np
from numpy import *

def main():
    
    arr=np.random.randint(10,51,size=11) #O(1)
    print(f"El arreglo es: {arr}") #O(1)
    arr = np.sort(arr) #O(1)
    print(f"El arreglo ordenado es: {arr}") #O(1)
    print("El nro mayor es el ultimo de la fila que estaria en la posicion 11 y que seria el nro:",arr[10]) #O(1)
    
    buscar=int(input("Que numero le gustaria buscar en el arreglo ordenado? ")) #O(1)
    
    index=np.searchsorted(arr,buscar) #O(N)
    
    if index < len(arr) and arr[index]==buscar:
        print(f"El numero {buscar} se encuentra en la siguiente posicion: {index}") #O(1)
    else:
        print(f"El numero {buscar} no se encuentra en el arreglo") #O(1)
main()