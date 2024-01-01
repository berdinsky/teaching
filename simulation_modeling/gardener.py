# one simulation run for the gardener problem 

import random

def simulate(T,m,s_0):
    s = s_0 # initially the state is s_0
    
    for i in range(0,m):
        n = random.random() # here we generate a random number
        if n<=T[s]['G']: 
            s='G'
        elif n<=T[s]['G']+T[s]['F']:
            s='F'
        else: 
            s='P'

        print(s)

# main program  

# transition matrix
T ={'G' : {'G' : 0.2, 'F' : 0.3, 'P' : 0.5}, 
    'F' : {'G' : 0.1, 'F' : 0.6, 'P' : 0.3}, 
    'P' : {'G' : 0.1, 'F' : 0.2, 'P' : 0.7}} 
    
m = 15 # number of iterations in one simulation run 

simulate(T,m,'G')