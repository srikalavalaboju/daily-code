"""#find sum of first N numbers
n=int(input())
sum=0
for i in range(1,n+1):
    sum +=i
print(sum) 

#multiplication
n=int(input())
for i in range(1,n+1):
    print(n,"x",i ,"=", n*i)
#factorial of a number
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
#Reverse of a number
n=int(input())
rev=0
while n > 0:
    digit=n%10
    rev = rev*10+digit
    n=n//10
print(rev)
#Reverse of a string
word = input("Enter:")
for i in range(len(word)-1,-1,-1):
    print(word[i],end=" ")
#find whether a number is prime
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count == 2:
    print("prime")        
else:
    print("Not prime")
#Print all prime numbers from 1 to N
n=int(input())
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=" ")
#Find the sum of digits of a number.
n=int(input())
sum=0
while n>0:
    digit = n%10
    sum+=digit
    n=n//10
print(sum)
#count num of digits
n=int(input())
count=0
while n>0:
    digit = n%10
    n=n//10
    count+=1
print(count)
#check whether a number is an armstrong number
n=int(input())
temp=n
pow=len(str(n))
sum=0
while temp>0:
    digit =temp%10
    sum+=digit**pow
    temp=temp//10
print(sum)
if sum == n:
    print("Armstrong")
else:
    print("Not armstrong")
#Check whether a number is a palindrome.
n=int(input())
temp=n
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
print(rev)
if rev == n:
    print("palindrome")
else:
    print("not a palindrome")
#print star
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
#reverse right angle stars
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
#print pyramid 
n=int(input())
for i in range(1,n+1):
    space=n-i
    star=2*i-1
    print(" "*space + "*"*star)
#Traditional method
n=int(input())
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end="")
    for star in range(2*i-1):
        print("*",end="")
    print()
#count vowels,consonants,digits and spaces in a string
w=input()
vowels=0
consonants=0
digit=0
space=0
for ch in w:
    if ch in "aeiouAEIOU":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digit+=1
    elif ch==" ":
        space+=1
print("vowels=",vowels)
print("consonants=",consonants)
print("Digit=",digit)
print("Space=",space)
#check whether two strings are anagram
string1=input()
str1=string1.lower()
sort1="".join(sorted(str1))
string2=input()
str2=string2.lower()
sort2="".join(sorted(str2))
if sort1==sort2:
    print("Anagram")
else:
    print("Not Anagram")
#bitwise operaters
a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
#list :stores multiple values in one variable
num=[10,20,30,40]
for x in num:
    print(x)
#sum of elements in list
nums=[10,20,30]
total=0
for x in nums:
    total+=x
print(total)"""
#find largest element
nums=[10,50,20,30]
larg=nums[0]
for x in nums:
    if x >larg:
        larg=x
print(larg)






    





        



