name = input("Enter employee name: ")
salary = float(input("Enter salary: "))
rating = int(input("Enter performance rating (1-5): "))
if rating == 5:
    bonus = 0.20 * salary
elif rating == 4:
    bonus = 0.15 * salary
elif rating == 3:
    bonus = 0.10 * salary
else:
    bonus = 0
final_salary = salary + bonus
print("\nEmployee Name:", name)
print("Performance Rating:", rating)
print("Bonus Amount: ", bonus)
print("Final Salary: ", final_salary)
