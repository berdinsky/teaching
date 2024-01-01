def DFS(G): 
    colour={} # pred, seen, done
    for i in G.keys(): 
        colour[i]="WHITE" # pred[i]=None     
    for i in G.keys(): 
        if colour[i]=="WHITE":
            DFSvisit(G,i,colour)
    
def DFSvisit(G,node,colour):
    stack=[]
    colour[node]="GREY" # seen[node]=time; time=time+1
    stack.append(node)
    
    print(node,' ') # printing node    
   
    while stack:
        
        u=stack[-1]
       
        whitenbr=False
        for i in G[u]:
            if colour[i]=="WHITE": 
                whitenbr=True  
                v=i
                break
        
        if whitenbr==True:    
            colour[v]="GREY" # pred[v]=u; seen[v]=time; time=time+1
            stack.append(v)
                    
            print(v) # printing node
        
        else: 
            stack.pop()
            colour[u]="BLACK" # done[u]=time; time=time+1
    return colour            
def main():
    
    # Test 1
    
    G1 = {0:[1,2],1:[0,2,3,4],2:[0,1,4,8],3:[1,5,6],4:[1,2,7,8],5:[3],
      6:[3],7:[4,8],8:[2,4,7]}
    
    print("For graph G1:") 
    
    DFS(G1)
    
    # Test 2

    G2 = {0:[1,2,3],1:[6],2:[0,4],3:[1,5,6],4:[5],5:[0,2,4,6], 6:[]}

    print("For graph G2:")
    
    DFS(G2)
    
    # Test 3 
    
    G3 = {0:[1], 1:[0],2:[3],3:[2]}
    
    print("For graph G3:")

    DFS(G3)
    
main()    