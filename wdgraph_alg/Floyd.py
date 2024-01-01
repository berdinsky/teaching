# Floyd algorithm 

import math

def Floyd(G):
    
    dist={}
    
    for u in G.keys(): # here we initialize the dist array
        row = {}
        for v in G.keys(): 
            if v in G[u].keys(): 
                row[v]=G[u][v]
            elif u==v:
                row[v]=0 
            else:      
                row[v]=math.inf
        dist[u]=row    
    
    for x in G.keys(): 
        for u in G.keys(): 
            for v in G.keys(): 
                dist[u][v]=min(dist[u][v],dist[u][x] + dist[x][v])  
    return dist  

def main(): 

    # Test 1 

    G1={0:{1:1,2:4},1:{3:2},2:{1:2,3:5},3:{0:2}}
    
    print(Floyd(G1))

    #Test 2 

    G2={0:{4:1,1:7,3:1},4:{1:5},3:{2:1},2:{1:2},1:{}}

    print(Floyd(G2))    

main()