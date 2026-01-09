#creating list
num=(10,20,40,90,10,"numbers")
print(num)
print(num[1])
print(num[-2])
print(num[0:3])
#methods
print(num.count(10))
print(num.index(90))
print(num)
#deleting indirectly
nums=list(num)
nums.pop()
num=tuple(nums)
print(num)
