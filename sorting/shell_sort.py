a=[1,5,7,1,3,4,8,0,5,3,-1,-3]
l=len(a)-1
gap = (4,3,1)
def insertionsort(a,h,j): 
    def dragleft(a,k): 
        a[(k+1)*h+j]=a[k*h+j]
        a[k*h+j]=c
        return a
    if  j <= l%h : 
        m=l//h + 1  
    else: 
        m=l//h
    for i in range(1,m): 
        c=a[i*h+j]
        k=i-1
        while k>=0 and a[k*h+j]>a[(k+1)*h+j]:
            dragleft(a,k)
            k=k-1
    return a

for i in range(0,len(gap)): 
    for j in range(0,gap[i]):
        insertionsort(a,gap[i],j)
print(a)
