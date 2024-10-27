infantiles= ["blancanieves", "los tres chanchitos", "cenicienta"]
novelas= ["don quijote", "la novicia revelde"]
policiales= ["sherlock holmes", "muerte en el nilo"]

def menu():
    global op
    op= input ("a. Ver libros disponibles / b. Eliminar libros / c. Agregar / d. Ver el stock de libros / e. Sair del sistema: ")  .lower()
    if op=="a":
        verL()
        menu()
    elif op=="b":
        borrarL()
        menu()
    elif op=="c":
        ingresarL()
        menu()
    elif op=="d":
        stockL()
        menu()
    elif op=="e":
        exit()
    else:
        print("Error")
        menu()
def verL():
    ver= (input("Ingrese que categoria quiere ver: a. Infantiles / b. Novelas / c. Policiales / d. Todas: ") ) .lower()
    if ver=="a":
        print(infantiles)
    elif ver=="b":
        print(novelas)
    elif ver=="c":
        print(policiales)
    elif ver=="d":
        print(infantiles+novelas+policiales)
    else:
        print("Error")
        verL()
def borrarL():
    print("Los libro disponibles son: ", infantiles, novelas, policiales)
    borrar= input("Que libro desea borrar: ") .lower()
    if borrar not in infantiles+novelas+policiales:
        print("Error")
        borrarL()
    if borrar in infantiles:
        infantiles.remove(borrar)
        print("Se borro el libro")
    if borrar in novelas:
        novelas.remove(borrar)
        print("Se borro el libro")
    if borrar in policiales:
        policiales.remove(borrar)        
        print("Se borro el libro")
def ingresarL():
    categoria=input("En que categoria desea ingresar el libro: ") .lower()
    ingresar= input("Que libro desea ingresar: ")
    if categoria=="infantiles":
        infantiles.append(ingresar)
        print("Se agrego el libro")
    elif categoria=="novelas":
        novelas.append(ingresar)
        print("Se agrego el libro")
    elif categoria=="policiales":
        policiales.append(ingresar)
        print("Se agrego el libro")
    else:
        print("Error")
        ingresarL()
def stockL():
    librosT= infantiles + novelas + policiales 
    stock= input("De que libro quiere ver el stock: ") .lower()  
    if stock not in librosT:
        print("Error")
        stockL()
    else:
        print(librosT.count(stock))

print("Bienvenido al sistema de gestión online de la biblioteca Nacional")
menu()
