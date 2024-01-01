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

def sortstraight(a):
    t=len(a); n=1
    while n<t: 
        m=n
        n=2*n
        if t>=n:
            for i in range(0,t//n):
                l=i*n
                s=l+m-1
                r=l+n-1
                merge(a,l,s,r)
        if t%n > m: 
            i=t//n
            l=i*n
            s=l+m-1           
            r=t-1           
            merge(a,l,s,r)      
    return a
print(sortstraight([4,2,3,9,0,-7,1,2,3,4,5,6,-8]))