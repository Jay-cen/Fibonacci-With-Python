fib_array = [0, 1]
a = 0
b = 1
dip = 10000
while ((a+b)<dip):
    a, b = b, a+b
    fib_array.append(b)

print(fib_array)