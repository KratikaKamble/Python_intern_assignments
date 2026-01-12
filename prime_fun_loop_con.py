def primes_in_range(start, end):
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ")

a = int(input("Enter start value: "))
b = int(input("Enter end value: "))
primes_in_range(a, b)
