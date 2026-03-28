
N=int(input("¿Cuántos números va a ingresar"))
numeros=[]
for x in range(N):
    n=float(input(f"Ingrese el numero {x+1}"))
    numeros.append(n)
b=int(input("¿Qué numero desea busacar?"))
if b not in numeros:
        print("El numero no esta en la lista")
else:
    for i in range(len(numeros)):
        if numeros[i]==b in numeros:
            p=i+1
            print(f"El numero {b}, fue encontrado en la posicion {p}")
        
