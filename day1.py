#linear search using Booolean
n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter the elements{i+1}:"))
    arr.append(val)
    print(arr)
found=False
key=int(input("Enter the target element:"))
for i in range(n):
    if arr[i]==key:
        found=True
        print("Element found")
        break
if not found:
    print("not found")
#without using Boolean
n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter the element{i+1}:"))
    arr.append(val)
    print(arr)
key=int(input("enter the key :"))
for i in range(n):
    if arr[i]==key:
        print("Element found")
        break
else:
    print("Element not found")