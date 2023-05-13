impares = list(filter(lambda x: x % 2 != 0, range(1, 1000))) #imprimir los números impares desde 1 hasta 999
print("Números impares:")
print(impares)
pares = list(filter(lambda x: x % 2 == 0, range(2, 1001))) #imprimir los números pares desde 2 hasta 1000
print("Números pares:")
print(pares)