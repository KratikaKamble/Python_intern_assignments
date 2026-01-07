def calculate_electricity_bill(units):
    if units<=100:
        bill=units*2
    elif units<=200:
        bill=(100*2)+(units-100)*4
    else:
        bill=(100*2)+(100*4)+(units-200)*6
    return bill
units=int(input("Enter electricity bill in units:"))
bill_total=calculate_electricity_bill(units)
print("Total bill : rupees ",bill_total)
    
