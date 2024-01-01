def BFS(G): 
    colour={} # pred, done
    for v in G.keys(): 
        colour[v]="WHITE" # pred[i]=None     
    for v in G.keys(): 
        if colour[v]=="WHITE":
            BFSvisit(G,v,colour)
    
def BFSvisit(G,node,colour):
    queue=[]
    colour[node]="GREY" # d[s]=0 
    queue.insert(0,node)
    
    print(node,' ') # printing node    
   
    while queue:
        
        u=queue[-1]
       
        for v in G[u]:
            if colour[v]=="WHITE": 
                colour[v]="GREY" # pred[v]=u; d[v]=d[u]+1   
                queue.insert(0,v)
                print(v)
        
        queue.pop()     
        colour[u]="BLACK"

    return colour            

def main():
    
    G1 = {0:[1,2],1:[0,2,3,4],2:[0,1,4,8],3:[1,5,6],4:[1,2,7,8],5:[3],
      6:[3],7:[4,8],8:[2,4,7]}

    G2 = {0:[1,2,3],1:[6],2:[0,4],3:[1,5,6],4:[5],5:[0,2,4,6], 6:[]}

    print("For graph G1:") 
    
    BFS(G1)
    
    print("For graph G2:")
    
    BFS(G2)
    
main()    