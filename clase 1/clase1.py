# rebeca Soberanis 
# 17-07-2023
# primer script con entrada, proceso y salida, calculando un precio de venta

#entrada 
precioCosto = float(input("captura el precio del costo: "))    #variable, espacio de memoria  precio neto, input("") es para capturar el dato Float= es un numero con decimal
utilidad = float(input("captura el porcentaje de utilidad: ")) /100   #variable, espacio de memoria porcentaje de utilidad 

#proceso
precioVenta = precioCosto + (precioCosto*(utilidad))

#salida
print("el precio de venta es: ", precioVenta)