def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while n > 0:
        d = n % 10
        total += d ** digits
        n //= 10

    if total == temp:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

num = int(input("Enter a number: "))
is_armstrong(num)
