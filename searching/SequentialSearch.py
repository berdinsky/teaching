def seqsearch(a,key): 
    for i in range(len(a)): 
        if a[i]==key: 
            return i
    return "the key has not been found"
def main(): 
    a=[2,5,7,1,8,9,10]
    result=seqsearch(a,1)
    print(result)
    
main() 