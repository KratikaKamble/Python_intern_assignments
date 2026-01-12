def fibonacci(n):
    a, b = 0, 1
    if n <= 0:
        print("Invalid input")
    elif n == 1:
        print(a)
    else:
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a, b = b, c

n = int(input("Enter number of terms: "))
fibonacci(n)
