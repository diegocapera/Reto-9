import timeit
def fibo(n : int )-> int:
  i : int = 1
  n1 : int = 0 # caso base
  n2 : int = 1
  while(i <= n):
    sumFibo = n1 + n2 #condicion
    n1 = n2 #actualizacion
    n2 = sumFibo
    i += 1
  return sumFibo
if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  start_time1 = timeit.default_timer()
  serieFibo = fibo(num)
  timer1= timeit.default_timer() - start_time1
  print(f"El ultimo valor de la serie {num} es {serieFibo}")

print(f"la serie tardo {timer1} en ejecutar")
def fiboRecursivo(n : int )-> int:
    if n <=1:
        return 1 #caso base
    else:
        return fiboRecursivo(n-1)+fiboRecursivo(n-2)  #condicion
if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  start_time2 = timeit.default_timer()
  serieFibo = fiboRecursivo(num)
  timer2 = timeit.default_timer() - start_time2
  print(f"El último número de la serie de Fibonacci hasta {num} es {serieFibo}")

print(f"fiboRecursivo se demoró {timer2} en correr")