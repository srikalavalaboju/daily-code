#Armstrong number
"""n=int(input())#153
temp=n
pow=len(str(n))#length digits 
digit=0
while temp>0:
    rem=temp%10#3,5,1
    digit+=rem**pow
    temp=temp//10#15,1
if digit==n:
    print("Armstrong number")
else:
    print("Not an Armstrong")
#even odd
n=int(input())
while n>0:
    if n%2==0:
        print("Even")
        break
    else:
        print("odd")
        break
#reverse of a number
n=int(input("Enter a Number:"))
rev=0
temp=n
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
print(rev)
#sum of odd Number
n=int(input("Enter a NUmber:"))
sum=0
for i in range(1,n+1):
    if i%2==1:
        sum+=i
print(sum)"""