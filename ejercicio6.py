N=int(input("¿Cuántos números va a ingresar"))
numeros=[]
for x in range(N):
    n=int(input(f"Ingrese el numero {x+1}"))
    numeros.append(n)
for i in range(len(numeros)):
    for j in range(len(numeros)):
        if i!=j:
            print(f"{numeros[i]};{numeros[j]}")