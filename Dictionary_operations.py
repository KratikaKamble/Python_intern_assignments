#creating dictionary
stud={42:"Kratika",54:"Ashwini",66:"Srushti",67:"Raksha",92:"abc"}
print(stud)
#accessing 
print(stud[54])
#accessing only keys
print(stud.keys())
#accessing only values
print(stud.values())
#changing values through keys
stud[92]="sasdssf"
stud[67]='Rakshita'
stud[92]='Kratika'
print(stud)
#methods
print(len(stud))
stud.pop(92)
print(stud)
stud.clear()
print(stud)
