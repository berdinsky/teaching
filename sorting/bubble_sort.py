a=[5,8,3,1,2,2,5,6,17,0,6,-1,6,7,7,2,19,-3,-5,1]

m = len(a) 

def swap(a,i): 
    s=a[i-1]
    a[i-1]=a[i] 
    a[i]=s
    return a
swapped=False

while swapped==False: 
    for i in range(1,m):
        if a[i]<a[i-1]: 
            swap(a,i)
            swapped=True
    if swapped==False: 
        break
    swapped=False    
print(a)