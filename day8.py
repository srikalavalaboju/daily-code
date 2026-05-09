#pizza order
"""print("PIZZA ORDER PROGRAM")
size=input("what is the size of pizza:")
bill=0
if size=="S" or size=="s":
    bill+=100
    print("You Ordered Small size Pizza")
elif size=="M" or size=="m":
    bill+=200
    print("You Ordered Medium size Pizza ")
elif size=="L" or size=="l":
    bill+=300
    print("You Ordered Large size Pizza ")

else:
    print("Add the Item to Cart")
pepperoni=input("Do you want Pepperoni(y/n)?")
if pepperoni =="y" or pepperoni=="Y":
    if size=="S" or size=="s":
        bill+=30
    else: 
        bill+=50

cheese=input("Do you want extra Cheese(y/n)?")
if cheese=="Y" or cheese=="y":
    if size=="S" or size=="s":
        bill+=20
    else:
        bill+=20

print(f"Your final bill is {bill} only...")"""

#Love score
name1=input("Enter your name:")
name2=input("Enter your gf/bf name:")
combine_string=name1+name2
combine_string.lower()
t=combine_string.count('t')
r=combine_string.count('r')
u=combine_string.count('u')
e=combine_string.count('e')
true=t+r+u+e
l=combine_string.count('l')
o=combine_string.count('o')
v=combine_string.count('v')
e=combine_string.count('e')
love=l+o+v+e
true_love=str(true)+str(love)
print(true_love,"%")


