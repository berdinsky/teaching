def merge(a,l,s,r):
    i=l; j=s+1; c=[]
    while i<=s and j<=r: 
        if a[i]<=a[j]: 
            c.append(a[i])
            i=i+1
        else: 
            c.append(a[j])
            j=j+1 
    while i<=s:
        c.append(a[i]); i=i+1 
    while j<=r: 
        c.append(a[j]); j=j+1
    for k in range(0,r-l+1): 
        a[l+k]=c[k]
    return a    

def mergesort(a,l,r):
    if l<r: 
        s=int((l+r)/2)
        mergesort(a,l,s)
        mergesort(a,s+1,r)
        return merge(a,l,s,r)
    else: 
        return a
a=[2,1,4,5,2,-9,8,8,56,-5,-3,5,5,2,1,4,1,0]
print(mergesort(a,0,len(a)-1))   