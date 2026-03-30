N=int(input("Ingrese un numero:"))
veces=0
while N>1:
    print(f"{N}/2={N//2}")
    N//=2
    veces+=1
print(f"Se dividió {veces} veces")