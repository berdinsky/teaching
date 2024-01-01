def DFS(G): 
    colour={} # pred, seen, done
    for i in G.keys(): 
        colour[i]="WHITE" # pred[i]=None; time=0    
    for i in G.keys(): 
        if colour[i]=="WHITE":
            recursiveDFSvisit(G,i,colour)
    
def recursiveDFSvisit(G,node,colour):
    colour[node]="GREY"  # seen[node]=time;  time=time+1
    
    print(node,' ') # printing node    
   
    for v in G[node]: 
        if colour[v]=="WHITE":             #pred[v]=node    
            recursiveDFSvisit(G,v,colour)
    colour[node]="BLACK" # done[s]=time;  time=time+1
                
def main():
    
    G1 = {0:[1,2],1:[0,2,3,4],2:[0,1,4,8],3:[1,5,6],4:[1,2,7,8],5:[3],
      6:[3],7:[4,8],8:[2,4,7]}

    G2 = {0:[1,2,3],1:[6],2:[0,4],3:[1,5,6],4:[5],5:[0,2,4,6], 6:[]}

    print("For graph G1:") 
    
    DFS(G1)
    
    print("For graph G2:")
    
    DFS(G2)
    
main()    