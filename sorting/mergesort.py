def merge(a,b):
    i=0; j=0; c=[]
    while i<len(a) and j<len(b): 
        if a[i]<=b[j]: 
            c.append(a[i])
            i=i+1
        else: 
            c.append(b[j])
            j=j+1 
    while i<len(a):
        c.append(a[i]); i=i+1 
    while j<len(b): 
        c.append(b[j]); j=j+1
    return c    

def mergesort(a):
    if len(a)>1: 
        m=int(len(a)/2)
        return merge(mergesort(a[0:m]),mergesort(a[m:len(a)]))
    else: 
        return a

print(mergesort([4,2,1,5,6,9,3,2,11,2]))