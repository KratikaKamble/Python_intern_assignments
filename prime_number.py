n=int(input("Enter the number:"))
count=0
for i in range(1,n+1):
    if n%1==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("not prime")
