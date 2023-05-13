# Reto-9

Punto 1

De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.
Punto 1.1
```python
squares = list(map(lambda x: (x, x**2), range(1, 101)))

for num, square in squares:
    print(num, ":", square)
```

Punto 1.2
```python
impares = list(filter(lambda x: x % 2 != 0, range(1, 1000))) #imprimir los números impares desde 1 hasta 999
print("Números impares:")
print(impares)
pares = list(filter(lambda x: x % 2 == 0, range(2, 1001))) #imprimir los números pares desde 2 hasta 1000
print("Números pares:")
print(pares)
```
Punto 1.3
```python
n = 10 #n es el número natural dado
numeros_pares_desendentes = sorted(filter(lambda x: x % 2 == 0 and x <= n and x >= 2, range(2, n+1)), reverse=True)
print(numeros_pares_desendentes)
```
Punto 2

De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).
Punto 2.1
```python
def imprimir_cuadrados(*args):
    for num in args:
        print(num, num**2)
imprimir_cuadrados(*range(1, 101))
```
Punto 2.2
```python
def sumar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado
print(sumar(1, 2, 3)) # output: 6
print(sumar(4, 5, 6, 7)) # output: 22
print(sumar(8, 9)) # output: 17
```
Punto 2.3
```python
def sumar(*args):
    if not args:
        return 0
    else:
        return args[0] + sumar(*args[1:])
resultado = sumar(*range(1, 51))
print(resultado)
```
Punto 3

Escriba una función recursiva para calcular la operación de la potencia.
```python
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
```
Punto 4

Utilice una plantilla para contar el tiempo en que se demora ejecutar la serie Fibonacci.
```python
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
```
Punto 5

Crear cuenta en stackoverflow y adjuntar imagen en el repo

![image](https://github.com/diegocapera/Reto-9/assets/124608110/f0362f1c-d42f-411e-8ca9-d1c882aecfb2)
 
 Punto 6
 
 Crear un perfil en Linkedin.
 
 ![image](https://github.com/diegocapera/Reto-9/assets/124608110/950eb1b6-dc8a-4b00-bfb3-eeeaccdbfbb8)

https://www.linkedin.com/in/diego-alejandro-guti%C3%A9rrez-capera-02b414159/
