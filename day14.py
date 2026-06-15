#list :stores multiple values in one variable
num=[10,20,30,40]
for x in num:
    print(x)
#sum of elements in list
nums=[10,20,30]
total=0
for x in nums:
    total+=x
print(total)
#find largest element
nums=[10,50,20,30]
larg=nums[0]
for x in nums:
    if x >larg:
        larg=x
print(larg)