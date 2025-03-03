import random                                                                # importamos la libreria random

print("Bienvenido al juego de piedra,papel,tijera o dianamita")
print("escoge tu opcion favorita")

                                                                             #lista = ["piedra", "papel", "tijera"]
                                                                             #print(lista)
                                                                             #lista.append ("dinamita")
                                                                             #print(lista) 
lista = ["piedra", "papel", "tijera", "dinamita"]                            # creamos la variable lista

# utilizamos el bucle while para  una estructura de control
# que permite repetir una sección de código mientras una
# condición específica sea verdadera


while True:                                                                  # dentro de la libreria random escogemos la opcion
    pc = random.choice(lista)                                                # choice que nos permite escoger cualquier
    jugador = None                                                           # opcion dentro de la lista al azar



# utilizamos el metodo lower ya que esta 
# convierte las mayusculas en minusculas

    while jugador not in lista:
         jugador = input("piedra, papel, tijera o dinamita?: "). lower()

    if jugador == pc:                                                     # utilizamos el condicional if porque este se utiliza para ejecutar 
        print("pc:", pc)                                                  # un bloque de código solo si se cumple una condición específica
        print("jugador:", jugador)
        print("empate!")

    elif jugador == "piedra":                                             # utilizamos el condicvional elif ya que este se utiliza para evaluar
        if pc == "papel":                                                 # múltiples condiciones en una estructura condicional
            print("pc:", pc)                                              # después de una primera condición if
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

# utilizamos el metodo lower ya que esta 
# convierte las mayusculas en minusculas

    jugar_de_nuevo = input("quieres jugar de nuevo? (si/no): ").lower()

    if jugar_de_nuevo != "si":
        break
print("Vuelve pronto ADIOS....!!!!!")
 
    


    

