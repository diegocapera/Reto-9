def imprimir_cuadrados(*args):
    for num in args:
        print(num, num**2)
imprimir_cuadrados(*range(1, 101))