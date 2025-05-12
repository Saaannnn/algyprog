import random as rand
import colorama, time
from colorama import *
colorama.init(autoreset=True)
from random import *
from time import sleep

def main():
    
    bot = rand.randint(0, 2)

    player = int(input("PIEDRA (0), PAPEL (1) o TIJERA (2): "))
    
    time.sleep(0.5)
    print("PIEDRA")
    time.sleep(0.5)
    print("PAPEL")
    time.sleep(0.5)
    print("o TIJERA")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print(f"Bot: {bot} VS. Player: {player}")

    if player == bot:
        print(Fore.YELLOW + "EMPATE")
    elif player == 0 and bot == 1:
        print(Fore.RED + "PERDISTE")
    elif player == 0 and bot == 2:
        print(Fore.GREEN + "GANASTE")
    elif player == 1 and bot == 0:
        print(Fore.GREEN + "GANASTE")
    elif player == 1 and bot == 2:
        print(Fore.RED + "PERDISTE")
    elif player == 2 and bot == 0:
        print(Fore.RED + "PERDISTE")
    elif player == 2 and bot == 1:
        print(Fore.GREEN + "GANASTE")

if __name__ == "__main__":
    main()
    while True:
        again = input("Quieres jugar de nuevo? (s/n): ").lower()
        if again == 's':
            main()
        else:
            print("Gracias por jugar!")
            break