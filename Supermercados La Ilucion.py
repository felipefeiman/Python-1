print("Supermercados La Ilusion")

nombre= input("Ingrese su nombre: ") 

verduleria= float (input(nombre + ", ingrese el monto que gasto en el sector verduleria: ") )
carniceria= float (input("Ingrese el monto que gasto en el sector carniceria: ") )
otros= float (input("Ingrese el monto que gasto en los demas sectores: ") )

gastoTotal= verduleria + carniceria + otros
descuento = gastoTotal * 0.9 

print(nombre + ", su gasto total fue: " + str(gastoTotal) )
print(nombre + ", tiene un descuento del 10%, su monto quedaría en: " + str(descuento))

print(nombre + ", gracias por usar nuestro sistema")
exit()