"""#list :stores multiple values in one variable
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
#find the smallest element in list
nums=[10,50,20,30]
small=nums[0]
for i in nums:
    if i<small:
        small=i
print(small)
#count even numbers
l=[10,15,20,25,30]
count=0
for x in l:
    if x%2==0:
        count+=1
print(count)
#count odd numbers
c_odd=[10,15,20,25,30]
count=0
for x in c_odd:
    if x%2==1:
        count+=1
print(count)
#reverse of a list
s=int(input())
nums=[]
for i in range(s):
    x=int(input())
    nums.append(x)
print(nums)
rev=[]
for l in range(len(nums)-1,-1,-1):
    rev.append(nums[l])
print(rev)
#second largest element in list
nums=[10,20,30,50,40]
large=nums[0]
sec_large=0
for x in nums:
    if x>large :
        sec_large=large
        large=x
    elif sec_large<x:
        sec_large=x
print(sec_large)
#check if list is sorted
nums=[]
for x in input().split():
    nums.append(int(x))
print(nums)
sorted_list=True
for i in range(len(nums)-1):#i is value not index
    if nums[i]>nums[i+1]:
        sorted_list=False
if sorted_list:
    print("sorted")
else:
    print("not sorted")
#remove duplicate
s=int(input())
num=[]
for i in range(s):
    x=int(input())
    num.append(x)
print(num)
new=[]
for x in num:
    if x not in new:
        new.append(x)
    else:
        continue
print(new)
#smallest element
list=[]
for x in input().split():
    list.append(int(x))
print(list)
small=list[0]
for i in list:
    if i<small:
        small=i
print(small)
#find the sum of all elements
li=[]
for i in input().split():
    li.append(int(i))
print(li)
sum=0
for x in li:
    sum+=x
print(sum)
#Find the average of elements.
i= int(input())
nums=[]
for x in range(i):
    s=int(input())
    nums.append(s)
print(nums)
sum=0
for s in nums:
    sum+=s
    avg=sum/len(nums)
print(avg)
#Merge two lists.
l1=[10,20,30]
l2=[40,50,60]
merg=[]
for x in l1:
    merg.append(x)
for x in l2:
    merg.append(x)
print(merg)
"""

"""##Dictionary:stores key value pair
student={
    "name":"sri",
    "Age":20
}
print(student["name"])
#add to dictionary
stud={"name":"sri","age":20}
stud["city"]="Hyderabad"
print(stud)"""
#user to enter values
Name=input("Enter name:")
Age=int(input("Enter Age:"))
City=input("Enter your city:")
student={"name":Name,"age":Age,"city":City}
print(student)









        