# linear time algorithm
a=[1,2,3,4,5,6,7,8,9,10,6,8,9,4]

m=int(len(a)/2)
s=0
t=0
for i in range(0,m):
    s=s+a[i]
    t = t + 1 #updating the number of elementary operations
print ('The sum of elements from',0,'to',m-1,'is:',s)
    
for j in range(0,m):    
    s = s + a[m+j]-a[j] 
    t = t + 2 #updating the number of elementary operations
    print ('The sum of elements from',j+1,'to',j+m,'is:',s)

print('The size of input is:',len(a))
print('The total number of elementary operations is:',t)    