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