import heapdict

def Prim(G,s):

    color={}; pred={}
 
    for u in G.keys():
        color[u]="WHITE"

    color[s]="GREY"
    
    Q = heapdict.heapdict() 
    
    Q[s]=0

    while bool(Q): 
                
        u = Q.popitem()[0]  # pop a node with the smallest key
        color[u]="BLACK"
        
        V = G[u] 

        for x in V.keys():
            t=V[x] 
            
            if color[x]=="WHITE": 
                color[x]="GREY"; pred[x]=u 
                Q[x]=t
            elif color[x]=="GREY":
                if (Q.get(x)>t): Q[x]=t; pred[x]=u
 

    return pred

def main(): 

    #Test 1 

    G1={0:{1:4,2:1,4:4},1:{0:4,4:3,5:4,3:2},2:{0:1,4:3},3:{1:2,5:1},
        4:{2:3,0:4,1:3,5:2},5:{1:4,3:1,4:2}}     
            
    print('For a graph G1:',Prim(G1,0)) 

    #Test 2 

    G2={0:{1:1,2:4,3:2},1:{0:1,2:2,3:2},2:{0:4,1:2,3:5},3:{0:2,2:5,1:2}}
     
    print('For a graph G2:',Prim(G2,0))

main()




    
