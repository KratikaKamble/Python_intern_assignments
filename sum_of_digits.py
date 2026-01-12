num = int(input("Enter a number: "))
sum_d= 0
if num < 0:
    num = -num   
while num > 0:
    digit = num % 10
    sum_d += digit
    num //= 10
print("Sum of digits:", sum_d)
