#rebeca soberanis 
# en este programa podemos ver el indice de masa corporal 

#entrada 
peso = float (input("Proporciona tu peso en kg:"))
estatura = float (input("Proporciona tu estatuta en mts:"))

imc = peso / estatura**2

#proceso 
print("Tu IMC es: ", imc)
if imc >= 30.00 : 
        #salida1
    print("Tu nivel de peso es obeso")
elif imc >= 25.00 :
        #salida2
    print("Tu nivel de peso es sobrepeso")
elif imc >= 18.5 :
        #salida3
    print("Tu nivel de peso es normal")
else :
        #Salida4
    print("Tu nivel de peso es bajo")
