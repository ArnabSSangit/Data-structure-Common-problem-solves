def occurances(arr,element):
    count=0
    aux = []
    for i in range(len(arr)):
        if arr[i]!=element:
            aux.append(arr[i])
        else:
            count=count+1           
    return aux+[0]*count     

arr=[1,2,3,4,4,5,6,7,4]   
occurances(arr,4) 
