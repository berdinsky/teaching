# example of an algorithm with nlog(n) running time

import sys
t=0
m=2
n = input('Enter an integer number: ')
if n.isdigit()==False: 
  sys.exit()   
n=int(n)
for i in range(1,n+1): 
    if i==m: 
        m=2*m
        for j in range(n): 
            t=t+1
print(t)       
      