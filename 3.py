def potencia(base, exponente):
  if exponente == 0:
    return 1
  elif exponente == 1:
    return base
  else:
    return base * potencia(base, exponente-1)
if __name__ == '__main__':
    base = float(input("Inserte una base de potencia: "))
    n = float(input("Inserte el exponente de la potencia: "))
    solucion = potencia(base, n)
    print(solucion)


