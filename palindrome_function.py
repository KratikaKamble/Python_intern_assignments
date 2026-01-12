def is_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    if temp == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"

num = int(input("Enter a number: "))
print(is_palindrome(num))
