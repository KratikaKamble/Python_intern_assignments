n=7
visitors=[]
print("Enter the number of visitors:\n")
for i in range(n):
    visitors.append(int(input()))
#for i in visitors:
 #   print(i)
#print("Highest visitors on the website",max(visitors))
#print("lowest visitors on the website",min(visitors))
highest=max(visitors)
lowest=min(visitors)
highest_day=visitors.index(highest)+1
lowest_day=visitors.index(lowest)+1
print("Highest visitors",highest,"on day",highest_day)
print("lowest visitors",lowest,"on day",lowest_day)
