name=input("Enter your name:")
age=int(input("Enter your age:"))
email=input("Enter your email ID:")
contact=input("Enter your contact number:")
graduation=float(input("Enter your percentage:"))
if age>=18:
    if graduation>=60:
        if len(contact)==10:
            print("Intern eligible")
        else:
            print("Contact number must contain 10 digits")
    else:
        print("Percentage must be above or equals to 60")
else:
    print("Age must be greater or equals to 18")
