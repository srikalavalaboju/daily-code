n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter the elements{i+1}:"))
    arr.append(val)
arr.sort()
print(arr)
key=int(input("Enter the key value:"))
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==key:
        print("Element found")
        break
    elif arr[mid]<key:
        low=mid+1
    else:
        high=mid-1
else:
    print("element is not found")
    
