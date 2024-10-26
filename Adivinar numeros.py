numero1= int (input("Jugador1, ingrese un numero entre 1 y 10: ") )
while numero1<1 or numero1>10:
    print("Error")
    numero1= int (input("Jugador1, ingrese un numero entre 1 y 10: ") )

print("Jugador 2, tienes 3 intentos para adivinar el numero del jugador 1")

intentos=3
puntos=3
while intentos>=1:
    numero2= int (input("Ingrese el numero del jugador 1: ") )
    if numero2==numero1:
        print("Ganaste, tienes", puntos, "puntos")
        break
    else:
        intentos-=1
        puntos-=1
        print("Te quedan", intentos, "intentos")
exit()