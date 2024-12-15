def fibonacci_yield(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        a = b
        b = a + b

        

print("fibonacci numbers with next")

for i in range(10):
    gen = fibonacci_yield(10)
    next(gen)    

print("fibonacci numbers with yield")
for i in fibonacci_yield(10):
    print(i)
