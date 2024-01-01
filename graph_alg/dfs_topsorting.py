def DFS(G): 
    colour={} # pred, seen 
    done=[]
    for i in G.keys(): 
        colour[i]="WHITE" # pred[i]=None; time=0    
    for i in G.keys(): 
        if colour[i]=="WHITE":
            DFSvisit(G,i,colour,done)
    return done 

def DFSvisit(G,node,colour,done):
    stack=[]
    colour[node]="GREY"  # seen[node]=time; time=time+1
    stack.append(node)
    
    while stack:
        
        u=stack[len(stack)-1]
       
        whitenbr=False
        for i in G[u]:
            if colour[i]=="WHITE": 
                whitenbr=True  
                v=i
                break
        
        if whitenbr==True:    
            colour[v]="GREY" # pred[v]=u; seen[v]=time; time=time+1
            stack.append(v)
        
        else: 
            stack.pop()
            colour[u]="BLACK"
            done.append(u) # time=time+1
    return colour,done

def main():
    
    G1 = {0:[1,2],1:[3,4],2:[3,4],3:[],4:[]}

    G2 = {0:[1],1:[2,3],2:[4,5],3:[],4:[],5:[]}    

    print("For graph G1:") 
    
 
    done=DFS(G1)
    
    done.reverse() 
    
    print(done)
    
    print("For graph G2:")
    
    done=DFS(G2)
    
    done.reverse() 
    
    print(done)    
    
main()    