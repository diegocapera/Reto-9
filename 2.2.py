def sumar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado
print(sumar(1, 2, 3)) # output: 6
print(sumar(4, 5, 6, 7)) # output: 22
print(sumar(8, 9)) # output: 17