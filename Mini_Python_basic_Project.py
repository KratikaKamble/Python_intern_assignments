#module 5:
def login(username, password):
    if username == "dd_admin" and password == "dd@123":
        print("Login Successful")
        return True
    else:
        print("Access Denied")
        return False
        
        
#module 1:
def emp_details():
#First login for access
    username = input("Enter username: ")
    password = input("Enter password: ")
    if not login(username, password):
        return
    
    
#module 1 code
    emp_id=input("Enter the employee ID:")
    name=input("Enter the name:")
    age=int(input("Enter the age:"))
    dept=input("Enter your department:")
    sal=float(input("Enter the basic salary:"))
    if age>=18 and sal>0:
        print("Employee registered successfully!")
    else:
        print("Sorry ,registeration denied because of age or salary")
        
        
#module 2:
    #n=5
    att=input("Enter the attendence of 5 days in(P/A):")
    lst=[]
    for i in range(1,6):
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
        
        
#module 3:
    def cal_sal(sal,count):
        HRA = sal*0.20
        DA = sal*0.10
        PF = sal*0.12
        net_sal=0
        if count<3:
            net_sal=sal-PF
            print(net_sal)
        else:
            net_sal=sal+HRA+DA-PF
            print(net_sal)
    cal_sal(sal,count)
    
    
#module 4:
    total = 0
    print("Enter 3 performance ratings (1 to 5):")
    for i in range(1, 4):
        rating = int(input(f"Rating {i}: "))
        total += rating
    avg = total / 3
    print("Average Rating:", avg)
    if avg >= 4:
        print("Performance: Excellent")
    elif avg >= 3:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")
emp_details()
