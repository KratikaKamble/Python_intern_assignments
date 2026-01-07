def check_intern_eligibility(age,percentage):
    if(age >=18 and percentage>=60):
        print("Eligible:Candidate is eligible for intern and meets criteria")
    else:
        print("Not Eligible:")
        if(age<18):
            print("Age is below 18")
        if(percentage<60):
            print("Percentage is below 60")
    return age,percentage
age=int(input("Enter your age:"))
percentage=float(input("Enter your percentage:"))
print(check_intern_eligibility(age,percentage))
