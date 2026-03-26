
numeros =  []
while True: 
    try :
        numero1 = int(input("Escriba su primer numero: "))
        numeros.append(numero1)
    except ValueError: 
        print("Error! tipo de dato no valido. Ingrese un numero")
    else: 
        break
while True: 
    try:    
        numero2 = int(input("Escriba su segundo numero: "))
        numeros.append(numero2)
    except ValueError: 
        print("Error! tipo de dato no valido. Ingrese un numero")
    else: 
        break
while True:
    try:
        numero3 = int(input("Escriba su tercer numero: "))
        numeros.append(numero3)
    except ValueError: 
        print("Error! tipo de dato no valido. Ingrese un numero")
    else:
        break
    
promedio = (sum(numeros)/len(numeros))

print(f"El promedio de sus numeros {numero1}, {numero2} y {numero3} es: {promedio:.2f}")

