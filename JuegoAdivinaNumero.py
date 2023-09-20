from random import *
nombre = input("¿Cual es tu nombre?: ")
print(f"Muy bien {nombre} vamos a jugar!")
print("he pensado un número entre 1 y 100 \ntienes solo 8 intentos para adivinar cuál crees que es el número \nA jugar!")
intentos = 8
numero_pensado = randint(1,100)
while intentos > 0:
    intento = int(input("Di cual crees que es ese numero: "))
# para ahorrar codigo el hace aqui el decremento de la variable intentos
    if intento < 0 or intento > 100:
        # el usa -> if intento not in range(1,101)
        print("Te atrape tramposo, el numero es entre el 1 y el 100, ingresa un numero valido")
        intentos -= 1
    elif intento < numero_pensado:
        print("No es ese, has dado un numero menor al que escogi")
        intentos -= 1
    elif intento > numero_pensado:
        print("No es ese, has dado un numero mayor al que escogi")
        intentos -= 1
    else:
        print(f"Felicidades has acertado! te ha tomado {9-intentos} intentos")
        break
if intentos == 0:
    print(f"No has podido ganar este juego \nbuena suerte para la proxima\nEl numero que pense era {numero_pensado}")
