n = int(input("Enter the number of terms to be included for generating Fibonacci Sequence"))
fib1 = 0
fib2 = 1
i = 1

if n == 1:
    print(fib1)
elif(n == 2):
    print(fib1,fib2)
else:
    print(fib1)
    print(fib2)
    while i <= n-2:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        print(fib)
        i += 1
