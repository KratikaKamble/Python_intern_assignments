course = input("Enter course name (Python / Data Analytics / AI & ML): ")
is_student = input("Are you a student? (yes/no): ")
early_reg = input("Early registration? (yes/no): ")
if course == "Python":
    fee = 5000
elif course == "Data Analytics":
    fee = 8000
elif course == "AI & ML":
    fee = 12000
else:
    print("Invalid course")
    exit()
discount = 0
if is_student == "yes":
    discount += 0.10 * fee
if early_reg == "yes":
    discount += 0.05 * fee
final_amount = fee - discount
print("\nCourse Name:", course)
print("Original Fee: ", fee)
print("Total Discount: ", discount)
print("Final Payable Amount: ", final_amount)
