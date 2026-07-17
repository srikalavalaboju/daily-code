"""#binary to decimal
s= input()
binary=s[::-1]
power=decimal=0
for i in binary:
    decimal+=int(i)*(2**power)
    power+=1
print(decimal)
#decimal to binary
s=int(input())
lst=[]
while s>0:
    rem=s%2
    lst.append(rem)
    s=s//2
rev=lst[::-1]
print("".join(map(str,rev)))
#decimal to octal
s=int(input())
string=""
while s>0:
    rem=s%8
    string+=str(rem)
    s=s//8
rev=string[::-1]
print(rev)
#octal to decimal
s=input()
rev=s[::-1]
power=octal=0
for i in rev:
    octal+=int(i)*(8**power)
    power+=1
print(octal)"""
#hexadecimal to decimal:
n=input().upper()
string=n[::-1]
digits="0123456789ABCDEF"
power=hexadecimal=0
for ch in string:
    value=digits.index(ch)
    hexadecimal+=value*(16**power)
    power+=1
print(hexadecimal)
"""#decimal to hexadecimal
s=int(input())
hexa_digit="0123456789ABCDEF"
result=""
while s>0:
    rem=s%16#10,1
    result+=hexa_digit[rem]
    s=s//16
print(result[::-1])"""





