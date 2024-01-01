def girth(G): 
    
    mincycle=len(G)+1 
    for v in G.keys():        
        cycle= BFSvisit(G,v) 
        if  cycle < mincycle: 
            mincycle = cycle 
    if mincycle<len(G)+1: 
        return mincycle 
    else: 
        return 'No cycles' 
    
def root_is_the_only_common_vertex(pred,root,u,v): 
    list_u=[]; list_v=[]
    w=u
    while not w==root: 
        list_u.append(pred[w]) 
        w=pred[w]
    w=v
    while not w==root:         
        list_v.append(pred[w]) 
        w=pred[w] 
    
    return len(set(list_u) & set(list_v))==1         
    

def BFSvisit(G,node):
    colour={}; pred={}; d={}
    for i in G.keys(): 
        colour[i]="WHITE"; pred[i]=None     
    
    colour[node]="GREY";  d[node]=0 
    
    queue=[]; queue.insert(0,node)
   

    cycle_len=len(G)+1; level=len(G)+1 
   
    while queue and d[queue[len(queue)-1]]<=level:
        
        u=queue[len(queue)-1]
       
        for v in G[u]:
            if colour[v]=="WHITE": 
                colour[v]="GREY"; pred[v]=u; d[v]=d[u]+1   
                queue.insert(0,v)
            elif colour[v]=="GREY": 
                if not root_is_the_only_common_vertex(pred,node,u,v): 
                    # the shortest cycle does not contain the root
                    return len(G)+1  
                else: 
                    level=d[u]
                    if d[u]+d[v]+1 < cycle_len:   
                        cycle_len=d[u]+d[v]+1 
        
        queue.pop()     
        colour[u]="BLACK"
    
    return cycle_len   

def main():
    
    G1 = {0:[1,2],1:[0,4,5],2:[0,3],3:[2,5,6],4:[1,6],5:[1,3,6],
      6:[3,4,5]}

    G2 = {0:[1,2],1:[0,4,5],2:[0,3,5],3:[2,6],4:[1,6,7],5:[1,2,7],6:[3,4,8],
          7:[4,5,8], 8:[6,7]}

    G3 = {0:[2],1:[3],2:[0,3],3:[1,2,4,5],4:[3],5:[3,6,7],6:[5],7:[5],8:[5]}
    print("For graph G1:") 
    
    print(girth(G1))
    
    print("For graph G2:")
    
    print(girth(G2))
    
    print("For graph G3:")
    
    print(girth(G3))
    
    
main()    