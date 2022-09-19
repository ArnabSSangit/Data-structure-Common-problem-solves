def  maxBunch(arr):
    n = len(arr)
    maxx=0
    i=0
    while i<n:
        count = 0
        ch  = arr[i]
        while(i<n and arr[i]==ch):
            i=i+1
            count +=1
        maxx=max(maxx,count)
    print(maxx)        


arr = [1,1,2,2,3,3,4,4,4,4,5,5]            
maxBunch(arr)
