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
    
emp_details()
