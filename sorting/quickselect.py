def medianofthree(a,i,j,k): 
    if a[i]<=a[j] and a[j]<=a[k]: 
        return j
    elif a[j]<=a[i] and a[i]<=a[k]:
        return i
    else: 
        return k
          

def swap(a,i,j):
    s=a[i] 
    a[i]=a[j] 
    a[j]=s
    return a

def partition(a,left,right,pivot): 
    swap(a,left,pivot)
    l=left; r=right     
    while l<r: 
        while a[r]>=a[left] and l<r:
            r=r-1
        while a[l]<=a[left] and l<r:
            l=l+1
        swap(a,l,r)     
    swap(a,left,l)     
    return a,l

def quickselect(a,l,r,k):
    if l<=r: 
        i=medianofthree(a,l,(l+r)//2,r) # choice of a pivot point
        a,j=partition(a,l,r,i)
        if j==k: 
            return a[j]
        else:
            if k<j: 
                return quickselect(a,l,j-1,k)
            else: 
                return quickselect(a,j+1,r,k)
   
a=[6,3,7,6,7,9,10,-4,-6,9,3,4,7]

print(quickselect(a,0,len(a)-1,1))