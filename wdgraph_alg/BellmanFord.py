import math

def BellmanFord(G,s):
    
    dist={}; n=len(G)
    
    for u in G.keys(): 
        dist[u]=math.inf

    dist[s]=0     

    for i in range(n): 
        for x in G.keys(): 
            Y=G[x] 
            for v in Y.keys():
                dist[v]=min(dist[v],dist[x]+Y[v]) 

    return dist             

def main(): 

    # Test 1 

    G1={0:{1:1,2:4},1:{3:2},2:{1:2,3:5},3:{0:2}}
    
    print(BellmanFord(G1,0))

    #Test 2 

    G2={0:{4:1,1:7,3:1},4:{1:5},3:{2:1},2:{1:2},1:{}}

    print(BellmanFord(G2,0))    

main()