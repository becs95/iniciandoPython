# rebeca soberanis 17/07/2023 
#Se procederá a realizar un programa que permitirá calcular cuanta propina se dejará basado en un porcentaje, ya sea el 10%, 15% o 20%

# entrada realizamos la asignacion de variables
totalConsumido = float(input("¿Cual fue el monto de la cuenta?: "))
porcentaje = int(input("¿Que porcentaje desea otorgar 10, 15, 30? "))/100
comensales = int(input("¿En cuantas personas se dividirá la cuenta?"))

#proceso
propina = totalConsumido * porcentaje # aqui sacamos la propina
totalCuenta = totalConsumido + propina #aqui sumamos la propina al consumo 
pagopp = totalCuenta / comensales # dividimos entre los comensales 

#salida 
print("Cada persona pagará: " ,pagopp )
print ("este es el pago final: ",totalCuenta )