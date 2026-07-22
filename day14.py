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
print(stud)
#user to enter values
Name=input("Enter name:")
Age=int(input("Enter Age:"))
City=input("Enter your city:")
student={"name":Name,"age":Age,"city":City}
print(student)
#loop through keys
name=input()
age=int(input())
city=input()
student={"name":name,"age":age,"city":city}
for key in student:
    print(key,student[key])
#updating student data
branch=input()
student={"marks":93,"branch":branch}
student["marks"]=99
print(student)
#check key exists
student={"name":"sri","age":20}
check=input()
if check in student:
    print("key found")  
else:
    print("key not found")
#Count the frequency of each character in a string using a dictionary.
s=input()
freq={}
for ch in s:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print(freq)
#Frequency of elements in a list
li=[10,20,10,30,20,10]
freq={}
for x in li:
    if x not in freq:
        freq[x]=1
    else:
        freq[x]=freq[x]+1
print(freq)
#most freq element in a list
list=[10,20,10,30,10]
freq={}
for x in list:
    if x in freq:
        freq[x]=freq[x]+1       
    else:
        freq[x]=1
print(freq)
lar_freq=0
for k in freq:
    if freq[k]>lar_freq:
        lar_freq=freq[k]
print(lar_freq)
#most frequent char
s=input()
dict={}
for i in s:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
lar_freq=0
for k in dict:
    if dict[k]>lar_freq:
        lar_freq=dict[k]
print(lar_freq)
#word freq
sentence="i like python i like coding"
word=sentence.split()
freq={}
for x in word:
    if x not in freq:
        freq[x]=1
    else:
        freq[x]=freq[x]+1
print(freq)
#find duplicate element in a list
list=[10,20,10,20,40]
seen=[]
duplicate=[]
for i in list:
    if i not in seen:
        seen.append(i)
    elif i not in duplicate:
        duplicate.append(i)
print(duplicate)
#first non repeating char
s=input()
freq={}
for ch in s:
    if ch not in freq:
        freq[ch]=1
    else:
        freq[ch]=freq[ch]+1
print(freq)
for key,value in freq.items():
    if value==1:
        print(key)
        break
#anagram
s=input()
w=input()
sort1=sorted(s)
sort2=sorted(w)
if sort1==sort2:
    print("anagram")
else:
    print("not a anagram")"""
"""
set stores unique values only

s={10,20,10,30}
print(s)
#giving user input
nums=[]
for i in input().split():
    nums.append(int(i))
print(nums)
#set:unordered collection of unique elements
s={10,"sri",20,"kala"}
print(s)
#list to set
lst=set([1,"sri",2,3])
print(lst)
#methods
s={1,2,3}
s1={3,2,4,5}
s.add(6)#adding
res=s.union(s1)#print(s|s1)
print(s-s1)#difference
print(s^s1)#removes the duplicates values itself
print(s&s1)#intersection res=s.intersection(s1)#common
s.clear()
print(s)
print(res)
#Tuple:immutable ordered collection of elements
tup=(0,1,"sri",3)
t=tuple("mummy")
print(tup)
print(t)
print(tup+t)
print(t[1:3])
del tup
print(tup)
#functions:block of code that performs a specific task
#1.No parameters,no return
def wel():
    print("Welcome to python")
wel()
#parameters,no return:
def par(a,b):
    print(a+b)
par(10,20)
#no parameter,return
def greet():
    print(100)
greet()
#parameter,return
def par_ret(a,b):
    return a*b
print(par_ret(5,4))
#even or odd:
def evenorodd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(evenorodd(5))
#larger number
def large(a,b):
    if a>b:
        return a
    elif a==b:

    else:
        return b
print(large(10,25))
#square
def square(n):
    return n**2
n=int(input())
print(square(n))
#length of string
def length(s):
    return len(str(s))
s=input()
print(length(s))
#factorial functions
def factorial(n):
    if n==0:
        return 1
    return (n)*factorial(n-1)
n=int(input())
print(factorial(n))
#largest ele in a list
def largest_ele(ele):
    large=ele[0]
    for i in range(1,len(ele)):      
        if ele[i]>large:
            large=ele[i]
    return large
ele=list(map(int,input().split()))
print(largest_ele(ele))
#smallest element in a list
def small(lst):
    small=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<small:
            small=lst[i]
    return small
lst=list(map(int,input().split()))
print(small(lst))
#reverse a string
def reve(wrd):
    reverse=""
    for ch in range(len(wrd)-1,-1,-1):
        reverse=reverse+wrd[ch]
    return reverse       
wrd=input()
print(reve(wrd))
#palindrome
def palin(w):
    reve=""
    for ch in range(len(w)-1,-1,-1):
        reve+=w[ch]
    if w==reve:
        return "palindrome"
    else:
        return "Not a palindrome"
w=input()
print(palin(w))
#count upper &lower case letter
def upp_low(s):
    upp_count=0
    low_count=0
    for ch in s:
        if ch.isupper():
            upp_count+=1
        elif ch.islower():
            low_count+=1
    return upp_count,low_count
s=input()
upper,lower=upp_low(s)
print("Uppercase=",upper)
print("lowercase=",lower)
#sum of digits 
def sum_of_digits(dig):
    rem=0
    while dig>0:
        digit=dig%10
        rem+=digit
        dig//=10
    return rem
dig=int(input())
print(sum_of_digits(dig))
#count the number of digits
def count_digits(num):
    count=0
    while num>0:
        digit=num%10
        count+=1
        num//=10
    return count
num=int(input())
print(count_digits(num))
#reverse a number
def reverse_num(num): 
    val="" 
    while num>0:
        dig=num%10
        val+=str(dig)
        num//=10        
    return int(val)
num=int(input())
digit=reverse_num(num)
print(digit,end="")
#check prime number
def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return "prime"
    else:
        return "Not prime"
num=int(input())
print(prime(num))
#fibonacci series
def fib(n):   
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        c=a+b
        a,b=b,c
n=int(input())
fib(n)
#GCD problem 
def gcd(n,s):
    if n<s:
        small=n
    else:
        small=s
    for i in range(1,small+1):
        if n%i==0 and s%i==0:
            gcd1=i
    return gcd1
n=int(input())
s=int(input())
print(gcd(n,s))
#lcm problem
def lcm(a,b):
    if a>b:
        larger=a
    else:
        larger=b    
    while True:
        if larger%a==0 and larger%b==0:
            return larger
        larger=larger+1
a=int(input())
b=int(input()) 
print(lcm(a,b))
#armstrong number
def arm(n):
    length=len(str(n))
    rem=0
    while n>0:
        digit=n%10
        rem=rem+digit**length
        n=n//10
    if n==rem:
        return "Armstrong"
    else:
        return "Not a Armstrong"
n=int(input())
print(arm(n))
#perfect number
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return "perfect Number"
    else:
        return "Not a perfect number"
n=int(input())
print(perfect(n))
#strong number
def strong(n):
    original=n
    sum=0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):            
            fact=fact*i
        sum+=fact
        n=n//10
    if sum==original:
        return "Strong Number"
    else:
        return "Not a strong number"
n=int(input())
print(strong(n))
#automorphic number
def auto(n):
    original=n
    leng=len(str(n))
    squ=n*n
    last=squ%(10**leng)
    if last==original:
        return "Automorphic number"
    else:
        return "Not automorphic number"    
n=int(input())
print(auto(n))"""
#harshad number
def harsh(n):
    sum=0
    original=n
    dig=n%10
    sum+=dig
    n//=10
    if n%sum==0:
        return "Harshad Number"
    else:
        return "Not a Harshad Number"
n=int(input())
print(harsh(n))














       