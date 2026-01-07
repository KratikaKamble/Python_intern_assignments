def check_password_strength(password):
    if len(password)<8:
        return "Weak password: password should contain atleast 8 characters"
    digit=False
    special=False
    chars="#@$&!"
    for ch in password:
        if ch.isdigit():
            digit=True
        if ch in chars:
            special=True
    if digit and special:
        return "Strong Password"
    else:
        return "Weak password: password with no digits and special characters"
pswrd=input("Enter your password:")
print(check_password_strength(pswrd))
