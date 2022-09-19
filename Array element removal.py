def removeElements(arr,idx):
    for i in range(0,len(arr)):
        if i == idx:
            arr[i]=0
arr =[10,20,30,40,50,60]
idx = 3
removeElements(arr,idx) 
print(arr) 
