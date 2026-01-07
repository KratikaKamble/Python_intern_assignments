def check_attendance(login_time):
    if login_time<9.30:
        return "Logined before 9:30 AM"
    elif 9.30<=login_time<=10.30:
        return "Login time is late"
    else:
        return "Absent"
login_time=float(input("Enter the login time:"))
print(check_attendance(login_time))
