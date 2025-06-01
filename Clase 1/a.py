import numpy as np
from numpy import *

def main():
  
    dif=int(input("Facil(1), Normal(2), Dificil(3): "))

    if dif==1:

        palabras = np.array(["amigos", "papaya", "llaves"])
        palabra = np.random.choice(palabras)
        jugar_ahorcado(palabra)
    
    elif dif==2:
        palabras = np.array(["personas", "haciendo", "bastante"])
        palabra = np.random.choice(palabras)
        jugar_ahorcado(palabra)

    elif dif==3:
        palabras = np.array(["presidente", "transporte", "desarrollo"])
        palabra = np.random.choice(palabras)
        jugar_ahorcado(palabra)
    
    else:
        print("No selecciono una dificultad valida")

def jugar_ahorcado(palabra, max_intentos=6):
    
    letras = list(palabra)
    descubiertas = ['_'] * len(letras)
    letras_usadas = set()
    intentos_restantes = max_intentos

    print("¡Bienvenido al Ahorcado!")
    print("Palabra a adivinar:", ' '.join(descubiertas))

    while intentos_restantes > 0 and '_' in descubiertas:
        print(f"\nIntentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {' '.join(sorted(letras_usadas))}")
        print("Palabra:", ' '.join(descubiertas))
        
        letra = input("Adivina una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Ingresa solo una letra válida.")
            continue

        if letra in letras_usadas:
            print("Ya intentaste con esa letra.")
            continue

        letras_usadas.add(letra)

        if letra in letras:
            print("¡Bien! Letra correcta.")
            for i, l in enumerate(letras):
                if l == letra:
                    descubiertas[i] = letra
        else:
            print("Letra incorrecta.")
            intentos_restantes -= 1

    if '_' not in descubiertas:
        print(f"\n¡Felicidades! Adivinaste la palabra: {palabra}")
    else:
        print(f"\n¡Perdiste! La palabra era: {palabra}")

main()