def calculate_discount(price,customer_type):
    if customer_type=="regular":
        discount=0.05
    elif customer_type=="premium":
        discount=0.15
    elif customer_type=="employee":
        discount=0.25
    else:
        return "Invalid customer"
    final_price=price-(price*discount)
    return final_price
price=float(input("Enter price:"))
customer_type=input("Enter your customer type(regular/premium/emplyoee):\n")
print(calculate_discount(price,customer_type))
