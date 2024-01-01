import math

def Dijkstra(G,s): 
    
    size = len(G)

    dist={}; color={}
    
    for u in G.keys():
        dist[u]=math.inf; color[u]="WHITE"

    dist[s]=0; color[s]="BLACK" 

    V=G[s]
    for x in V.keys():
        dist[x]=V[x]    
    
    index = 1  
    while index<size:
      
        # easy and simple, but inefficient way to get the next vertex
        u = sorted(dist.items(),key=lambda t: t[1])[index][0]     

        color[u]="BLACK"

        V=G[u]
        for x in V.keys(): 
            if color[x]=="WHITE":
                dist[x]=min(dist[x],dist[u]+V[x]) 
        
        index = index + 1
    
    return dist 

def main():

    # Test 1 

    G1={0:{1:1,2:4},1:{3:2},2:{1:2,3:5},3:{0:2}}
    
    print(Dijkstra(G1,0))

    #Test 2 

    G2={0:{4:1,1:7,3:1},4:{1:5},3:{2:1},2:{1:2},1:{}}

    print(Dijkstra(G2,0))

main()