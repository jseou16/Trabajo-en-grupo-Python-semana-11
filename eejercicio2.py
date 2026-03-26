numeros = int(input("Cuántos números vas a poner?: "))
num = int(input("Ingrese número 1: "))
mayor = num
menor = num

for i in range(2, numeros + 1):
    num = int(input("Ingrese número " + str(i) + ": "))

    if num > mayor:
        mayor = num

    if num < menor:
        menor = num

print("El número mayor es: " + str(mayor))
print("El número menor es: " + str(menor))