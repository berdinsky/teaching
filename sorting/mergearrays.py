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

print(merge([0,1,5],[2,3,7,9,10]))