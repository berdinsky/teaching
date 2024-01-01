f1=1
f2=1

n=input('Enter a positive integer:')
n=int(n)
print(f1)
print(f2)
for i in range(3,n+1): 
    h=f2
    f2=f1+f2
    print(f2)
    f1=h
