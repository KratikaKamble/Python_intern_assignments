dist=int(input("Enter the distance in km:"))
if dist<=5:
    print("Local")
elif dist>6 and dist<20:
    print("City distance")
else:
    print("Outstation")
