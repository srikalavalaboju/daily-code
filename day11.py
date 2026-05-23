#CALCULATOR
number1 = float(input("Enter the first Number:"))
number2 = float(input("Enter the Second Number:"))
print("_____Arthimetic Operations_____")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = input("Enter Your choice ?")
#Addition
if choice == "1":
    add = number1 + number2
    print("Result=",add)
#subtraction
elif choice == "2" :
    sub = number1 - number2
    print("Result = ",sub)
#Multiplication
elif choice == "3":
    mul = number1 * number2
    print("Result =",mul)
#Division
elif choice == "4":
    if number2 != 0 :
        div = number1 / number2
        print("Result = ",div)
    else:
        print("Zero Division Error....")
else :
        print("Invalid choice")