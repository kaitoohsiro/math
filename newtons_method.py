x = 3

# y = x**2

while True:
    x2 = x - (x ** 2 - 3) / (2 * x)

    if abs(x2 - x) < 0.00001:
        break

    x = x2

print(x)