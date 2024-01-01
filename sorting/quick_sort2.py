from random import randrange

def medianofthree(a,i,j,k): 
    if a[i]<=a[j] and a[j]<=a[k]: 
        return j
    elif a[j]<=a[i] and a[i]<=a[k]:
        return i
    else: 
        return k
          

def swap(a,i,j):
    s=a[i]; a[i]=a[j]; a[j]=s
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

def quicksort(a,l,r):
    if l<r: 
        i=randrange(l, r)  # choice of a pivot point
        a,j=partition(a,l,r,i)
        quicksort(a,l,j-1)
        quicksort(a,j+1,r)
    return a

a=[6,5,4,5,6,-4,4,1,1,0,-9,7,8,8,4,2,1,3]

print(quicksort(a,0,len(a)-1))