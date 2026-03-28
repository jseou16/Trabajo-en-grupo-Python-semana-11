while True: 
    try: 
        cuantosNumeros = int(input("Cuantos numeros va a ordenar? "))
    except ValueError:
        print("Error! Ingrese solo un numero")
    else:
        break

numeros = []

for n in range(cuantosNumeros):
    try:
        numero = float(input(f"Escriba su numero #{n+1}: "))
        numeros.append(numero)
    except ValueError: 
        print("Error! Ingrese solo numeros")

listaDesorden = numeros.copy()
totalNumeros = len(numeros)

for i in range(totalNumeros):
    for k in range(0, totalNumeros - i - 1):
        if numeros[k] > numeros[k+1]:
            numeros[k],numeros[k+1] = numeros[k+1],numeros[k]

print(f"La lista original es: {listaDesorden}")
print(f"La lista ordenada es: {numeros}")