peliculas= ["rambo", "norhinf hill", "patch adams", "locademia de policia"]

def mail():
    contador=0
    correo= input("Ingrese su correo electronico: ") .lower()
    for i in correo:
        if i=="@":
            contador+=1
    if contador!=1:
        print("Error")
        mail()
def comprarP():
    pelicula= input("Que película desea ver: ") .lower()
    for i in peliculas:
        if i==pelicula:
            print("Se eligio la pelicula")
            break
    else:
        print("Error")
        comprarP()
def comprarE():
    entradas= int (input ("Ingrese la cantidad de entradas que desea, cada una vale $1000: ") )
    print("Tiene que adivinar el director de la película ET. La cantidad de oportunidades que tiene para adivinarlo es igual a la cantidad de entradas que adquirió")
    director1= "steven spielberg"

    for i in range (entradas):
        director2= input("Ingrese el director: ")
        if director2==director1:
            print("Ganaste, tu costo es:", "$"+entradas*1000*0.5)
            break
        else:
            print("Error")
    else: 
        print("No obtuvo el descuento, disfrute la pelicula")
    exit()

print("Bienvenido al Cine La plata")
mail()
comprarP()
comprarE()