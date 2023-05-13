n = 10 #n es el número natural dado
numeros_pares_desendentes = sorted(filter(lambda x: x % 2 == 0 and x <= n and x >= 2, range(2, n+1)), reverse=True)
print(numeros_pares_desendentes)