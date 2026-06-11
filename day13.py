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
if n%2==1:
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
    print("Not armstrong")"""
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


        



