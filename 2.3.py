def sumar(*args):
    if not args:
        return 0
    else:
        return args[0] + sumar(*args[1:])
resultado = sumar(*range(1, 51))
print(resultado)