opening_stock=[85,90,185,725]
closing_stock=[75,95,185,223]
for i in range(len(opening_stock)):
    if closing_stock[i]>opening_stock[i]:
        print(f"Product {i+1}:Closing Stock is Increased")
    elif opening_stock[i]>closing_stock[i]:
        print(f"Product {i+1}: Closing Stock is Reduced")
    else:
        print(f"Product {i+1}:No Changes in closing and opening stock")
