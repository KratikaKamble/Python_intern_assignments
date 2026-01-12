def sum_even_odd(lst):
    even_sum = 0
    odd_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    print("Sum of Even numbers:", even_sum)
    print("Sum of Odd numbers:", odd_sum)


n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    numbers.append(int(input("Enter number: ")))

sum_even_odd(numbers)
