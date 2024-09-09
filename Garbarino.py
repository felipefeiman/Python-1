def comprarElectrodomesticos():
    compraE= (input("Tiene estos porductos disponibles: " "a. Heladera " "b. TV " "c. Licuadora ") ) .lower()

    if compraE=="a":
        costoE=50000
        print("Su gasto en electrodomesticos fue de", costoE)
    elif compraE== "b":
        costoE=35000
        print("Su gasto en electrodomesticos fue de", costoE)
    else:
        costoE=5000
        print("Su gasto en electrodomesticos fue de", costoE)
    return costoE
def comprarMusica():
    compraM= (input("Tiene estos discos disponibles: " "a. Queen " "b. Muse " "c. The Beatles ") ) .lower()

    if compraM=="a":
        costoM=500
        print("Su gasto en musica fue de", costoM)
    elif compraM=="b":
        costoM=300
        print("Su gasto en musica fue de", costoM)
    else:
        costoM=450
        print("Su gasto en musica fue de", costoM)
    return costoM
def comprarAmbos():
    Ecosto=comprarElectrodomesticos()
    Mcosto=comprarMusica()

    costoT= Ecosto + Mcosto
    print("Su gasto total fue:",costoT)

nombre= input("Ingrese su nombre: ")
print("Bienvenido",nombre,"al sistema Garbarino")

op=input("¿Que desea comprar? a. Comprar electrodomesticos / b. Comprar musica / c. Ambos ") .lower()

if op=="a":
    comprarElectrodomesticos()
    exit()
elif op=="b":
    comprarMusica()
    exit()
else:
    comprarAmbos()
    exit()