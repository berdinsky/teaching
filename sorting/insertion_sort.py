a=[5,8,3,1,2,2,5,6,7,0,6,-1,6,7,7,2,19,-3,-5,1]

m=len(a)

def swap(a,k):
    s=a[k+1] 
    a[k+1]=a[k]
    a[k]=s
    return a

for i in range(1,m): 
    k=i-1
    while k>=0 and a[k]>a[k+1]:
        swap(a,k)
        k=k-1
print(a)