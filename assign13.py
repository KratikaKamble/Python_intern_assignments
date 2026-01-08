#Student passed or fail
marks=float(input("Enter your marks:"))
att=float(input("Enter the attendance in percentage:"))
if marks> 40 and att> 75:
    print("Pass!!! ")
else:
    print("Fail!!")
6589
#login
user="krarak"
email="kr@1528"
username=input("Enter your username or email-id:")
if username==user or username==email:
    print("Login Successful!!")
else:
    print("Access Denied!!")

#not operator
is_suspended=bool(input("Enter suspended or not (True/False):"))
if is_suspended== True:
    print("Active")
    print(not(is_suspended))
if is_suspended== False:
    print("Inactive")

    
