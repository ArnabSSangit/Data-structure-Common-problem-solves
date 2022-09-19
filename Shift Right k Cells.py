def arrshiftRight(arr,k): 
    for i in range(0,k):
        arr[k+i]=arr[i]
    for i in range(0,k):
        arr[i]=0      

arr=[10,20,30,40,50,60]
k=3
arrshiftRight(arr,k)
print(arr)
