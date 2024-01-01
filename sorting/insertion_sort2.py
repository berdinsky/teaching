a=[5,8,3,1,2,2,5,10,7,0,6,-1,6,7,7,2,19,-3,-5,1]

m=len(a)

def drag(a,k): 
    a[k+1]=a[k]
    a[k]=p
    return a

for i in range(1,m): 
    p=a[i]
    k=i-1
    while k>=0 and a[k]>a[k+1]:
        drag(a,k)
        k=k-1
for i in range(0,m): 
    print(a[i])