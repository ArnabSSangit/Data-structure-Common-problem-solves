def arrshiftleft(arr,k):
    for i in range(0,k):
        arr[i]=arr[k+i]
    for i in range(k,len(arr)):
        arr[i]=0
arr=[10,20,30,40,50,60]
k=3
arrshiftleft(arr,k)
print(arr)      
