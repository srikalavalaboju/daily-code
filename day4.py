#selection sort
# n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter the elements{i+1}:"))
    arr.append(val)
print("Before sorted array",arr)
for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=arr[j]
print("After sorted array:",arr)