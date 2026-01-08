#relational operators
age=int(input("Enter your age:"))
if age>=18:
    print("Voter is eligible to vote!!! ")
else:
    print("You are not eligible to vote:( ")
    
#Employee salary comparision
emp1=float(input("Enter emp1 salary:"))
emp2=float(input("Enter emp2 salary:"))
emp3=float(input("Enter emp3 salary:"))
if emp1>emp2:
    if emp1>emp3:
        print("Employee 1 has higher salary")
    else:
        print("Employee 3 has higher salary")
else:
    if emp2>emp3:
        print("Employee 2 has higher salary")
    else:
        print("Employee 3 has higher salary")

#login pin correctness
pin="just_we2023"
pwrd=input("Enter PIN:")
if pwrd==pin:
    print("Hurray!! Login Successful!!")
if pwrd!=pin:
    print("Oops!! Access Denied")


    
