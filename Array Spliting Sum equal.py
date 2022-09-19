def splitingSum(arr):
    rightS = 0
    leftS=0
    for i in range(0,len(arr)):
        rightS+=arr[i]
    for i in range(0,len(arr)):
        rightS -= arr[i]
        leftS +=arr[i]
        if rightS == leftS:
            return True

    return False

arr=[1,1,5,2,1]    
splitingSum(arr)  
