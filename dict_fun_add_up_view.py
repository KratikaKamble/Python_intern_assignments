stud={}
def add_stud(name,marks):
    
    stud[name]=marks
    print("Student added successfully")
def update_stud():
    name=input("Enter the student name uh want to update:")
    if name in stud:
        marks=float(input("Enter the marks of the student:"))
        stud[name]=marks
        print("Updated successfully")
    else:
        print("required student not found")
    
def view_stud():
    if not stud:
        print("Student details not available")
    else:
        for name,marks in stud.items():
            print(name,":",marks)
    
n=int(input("Enter the number of students:"))
for i in range(n):
    name=input("Enter the name of the student:")
    marks=float(input("Enter the marks of the student:"))
    add_stud(name,marks)
update_stud()
view_stud()
    
