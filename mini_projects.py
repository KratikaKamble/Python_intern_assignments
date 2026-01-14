def emp_details():
    emp_id=input("Enter the employee ID:")
    name=input("Enter the name:")
    age=int(input("Enter the age:"))
    dept=input("Enter your department:")
    sal=float(input("Enter the basic salary:"))
    if age>=18 and sal>0:
        print("Employee registered successfully!")
    else:
        print("Sorry ,registeration denied because of age or salary")
    n=5
    att=input("Enter the attendence of 5 days in(P/A):\n")
    lst=[]
    for i in range(n):
        lst.append(input())
    count=0
    for i in lst:
        if i=="P":
            count+=1
    if count>=4:
        print("Regular")
    elif count==3:
        print("Warning")
    else:
        print("Irregular")
emp_details()
