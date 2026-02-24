#bubble sort
n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter the element {i+1}:"))
    arr.append(val)
print("before sorted:",arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("After sorted:",arr)
#selsection sory
n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter the elements{i+1}:"))
    arr.append(val)
print("before sorted:",arr)
for i in range(n-1):
    mid_index=i
    for j in range(i+1,n):
        if arr[j]<arr[mid_index]:
            mid_index=j
        arr[i],arr[mid_index]=arr[mid_index],arr[i]
print("After sorted:",arr)
        
