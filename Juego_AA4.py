import random

lista = ["piedra", "papel", "tijera"]
print(lista)
lista.append ("dinamita")
print(lista) 

lista = ["piedra", "papel", "tijera", "dinamita"]

while True:
    pc = random.choice(lista)
    jugador = None


    while jugador not in lista:
         jugador = input("piedra, papel, tijera o dinamita?: "). lower()

    if jugador == pc:
        print("pc:", pc)
        print("jugador:", jugador)
        print("empate!")

    elif jugador == "piedra":
        if pc == "papel":
            print("pc:", pc)
            print("jugador:", jugador)
            print("perdiste!")
        if pc == "tijera":
            print("pc:", pc)
            print("jugador:", jugador)
            print("ganaste!")
        if pc == "dinamita":
            print("pc:", pc)
            print("jugador:", jugador)
            print("perdiste!")

    elif jugador == "papel":
        if pc == "tijera":
            print("pc:", pc)
            print("jugador:", jugador)
            print("perdiste!")
        if pc == "piedra":
            print("pc:", pc)
            print("jugador:", jugador)
            print("ganaste!")
        if pc == "dinamita":
            print("pc:", pc)
            print("jugador:", jugador)
            print("perdiste!")

    elif jugador == "tijera":
        if pc == "piedra":
            print("pc:", pc)
            print("jugador:", jugador)
            print("perdiste!")
        if pc == "papel":
            print("pc:", pc)
            print("jugador:", jugador)
            print("ganaste!")
        if pc == "dinamita":
            print("pc:", pc)
            print("jugador:", jugador)
            print("ganaste!")

    elif jugador == "dinamita":
        if pc == "piedra":
            print("pc:", pc)
            print("jugador:", jugador)
            print("ganaste!")
        if pc == "papel":
            print("pc:", pc)
            print("jugador:", jugador)
            print("ganaste!")
        if pc == "tijera":
            print("pc:", pc)
            print("jugador:", jugador)
            print("perdiste!")
    
    jugar_de_nuevo = input("quieres jugar de nuevo? (si/no): ").lower()

    if jugar_de_nuevo != "si":
        break
print("adios")
 
    


    

