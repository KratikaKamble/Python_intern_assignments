#Arithematic operators
bill=float(input("Enter the amount:"))
GST=bill*0.18
print("GST added=",GST)
total_amt=GST+bill
print("Total price of the product=",total_amt)

#finding remainder
stud=int(input("Enter the total number of students:"))
grp=int(input("Enter the total number of groups:"))
remain_std=stud%grp
print("Total number of remaining students :",remain_std)

#exponential
volt=int(input("Enter the voltage used:"))
res=int(input("Enter resistance in ohms:"))
power=volt**2/res
print("Total power consumption is :",power)


