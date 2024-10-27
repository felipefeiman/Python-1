print("Automotores Carlitos")


gasto=int (input("Ingrese el monto que desea gastar: ") )
if gasto<1000000:
   print("No hay autos de ese valor")
   gasto=int (input("Ingrese el monto que desea gastar: ") )
   if gasto<1000000:
      print("Gracias por usar nuestro sistema")
      exit()

marca=str (input("Ingrese la marca que esta buscando: ") ) .lower()   
if marca!="ford" and marca!="chevrolet":
   print("No hay autos de esa marca")
   marca=str (input("Ingrese la marca que esta buscando: ") ) .lower()
   if marca!="ford" and marca!="chevrolet":
      print("Gracias por usar nuestro sistema")
      exit()

puertas=int (input("Ingrese el numero de puertas que esta buscando: ") )
if puertas>5 or puertas<3:
   print("No hay autos con esa cantidad de puertas")
   puertas=int (input("Ingrese el numero de puertas que esta buscando: ") )
   if puertas<5 or puertas>3:
      print("Gracias por usar nuestro sistema")
      exit()


if gasto>3000000 and gasto<6000000 and marca=="chevrolet":
   print("Esta disponible la Chevrolet Tracker") 

elif gasto>5000000 and marca=="ford" and puertas==3:
   print("Esta disponible la Ford Ranger") 

elif gasto<4000000 and marca=="ford" and puertas==4:
   print("Esta disponible la Ford Eco Sport") 

elif gasto<2000000 and marca=="chevrolet" and (puertas==3 or puertas==5):
   print("Esta disponible la Chevrolet Corsa") 

else:
   print("No hay autos con esas caracteristicas")
   print("Gracias por usar nuestro sistema")
   exit()
