def binarySearch1(a,key): 
    l=0; r=len(a)-1
    while l<=r: 
        i=(l+r)//2
        if a[i]<key:
            l=i+1
        elif a[i]>key:
            r=i-1
        else: 
            return i
    return "the key has not been found"
def main(): 
    a=[2,5,7,11,18,19,20,22,24,28,31,43]
    result=binarySearch1(a,11)
    print(result)
    
main() 