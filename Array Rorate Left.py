def rorateLeft(source,k):
    for i in range(0,k):
        for i in range(1,len(source)):
            temp = source[i]
            source[i]=source[i-1]
            source[i-1] = temp
        
      
if __name__ =="__main__":
    source=[10,20,30,40,50,60]
    k=3
    rorateLeft(source,k)
    print(source)
