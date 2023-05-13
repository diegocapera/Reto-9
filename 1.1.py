squares = list(map(lambda x: (x, x**2), range(1, 101)))

for num, square in squares:
    print(num, ":", square)