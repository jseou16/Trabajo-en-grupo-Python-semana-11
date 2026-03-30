#Ejercicio1.py 
#Tiene complejidad O(1) ya que al tener un numero de datos fijo, no cambia su tiempo de ejecucion segun la "cantidad" de datos, como si lo haria en otras complejidades

# Ejercicio2.py

# Complejidad O(n):
# Porque el programa recorre los números una sola vez.
# Si el usuario ingresa n números, el ciclo hace comparaciones para cada número, una por una, sin ciclos anidados. Es decir, el Primer número se usa para inicializar, mientras que los otros n - 1 números: se recorren una vez
#  También es:
# O(1):
# Ya que el programa no guarda todos los números en una estructura como lista. El espacio usado es constante.

#Ejercicio3.py
#Este tiene una complejidad de O(n) ya que al tener la lista busca uno por uno dentro de la misma buscando el numero que le pedimos

#Ejercicio4.py 
#Este tiene complejidad O(n^2) ya que tiene dos loops uno dentro del otro, y cada que el de dentro funciona tiene que revisar todos los valores del de fuera, siendo como el ejemplo de clase del "todos contra todos", un n^2

#Ejercicio5.py
#El ejercicio 5 es una escala logaritmica tiene O(logn) porque va dividiendo el numero en 2 cada vez hasta llegar a uno, como una escala logaritmica log2, por lo que siempre llega a 1 y se normaliza despues de un numero de iteraciones no muy extenso


#Ejercicio6.py
#El ultimo ejercicio tiene un O(n^2) igual que el 4to, ya que al igual que dicho ejercicio tiene dos loops for que revisan siempre todos los datos para hacer pares de los numeros ordenados
