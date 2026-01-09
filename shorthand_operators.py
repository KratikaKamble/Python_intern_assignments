#wallet balance checking after shopping
pre_wallet=float(input("Enter the balance in the wallet:"))
spent=float(input("Enter the amount spent after shopping:"))
pre_wallet-=spent
print("total amount in the wallet after shopping is:",pre_wallet)

#score checking
pre_score=int(input("Enter the previous score:"))
up_score=int(input("Enter the score made:"))
pre_score+=up_score
print("total score is:",pre_score)

#stock checking after sales
pre_stock=int(input("Enter the previous stock:"))
sales=int(input("Enter the sales made:"))
pre_stock-=sales
print("total stock present after sales:",pre_stock)
