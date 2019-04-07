fib = 0
num = 0
num2 = 1
print(num2, end=' ')
while fib < 980:
    fib = num + num2
    num = num2
    num2 = fib
    print(fib, end=' ')
