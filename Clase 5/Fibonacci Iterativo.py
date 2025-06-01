def main():
    p=0
    s=1
    print("Indique numero entero positivo mayor que 0 correspondiente a la cantidad")
    print("de numeros de la secuencia a ser mostrados")
    c=int(input())
    print("Los ",c," primeros numeros de la secuencia de fibonacci son:")
    if(c==1):
        print(p,end=".")
    elif(c==2):
        print(p,end=", ")
        print(s,end=".")
    else:
        print(p,end=",")
        print(s,end=",")    
        cont=2
        while(cont<c):
            f=(p+s)
            cont+=1
            if(cont<c):
                print(f,end=",")
            else:
                print(f,end=".")
            p=s
            s=f        
    print()        

main()