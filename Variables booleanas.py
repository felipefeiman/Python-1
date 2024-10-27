print("Sistema de selección de deporte")

genero= (input("Diga su genero: ") ) .lower()
edad=int (input("Diga su edad: ") )
altura=float (input("Diga su altura: ") )

hombre=genero== "hombre" or genero== "varon" or genero== "masculino"
print("Hombre: " , hombre)
mayor=edad>18
print("Mayor de edad: " , mayor)
alto=altura>1.8 
print("Alto: " , alto)

print("Puede jugar rugby: " , hombre)

mujerAlta=genero!=hombre and alto
print("Puede jugar al voley: " , mujerAlta)

basket= hombre and alto
print("Puede jugar al basket: " , basket)

futbol= hombre and edad<50
print("Puede jugar al futbol: " , futbol)

exit()
