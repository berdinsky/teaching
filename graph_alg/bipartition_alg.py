def Bipartition(G): 
    colour={}; blue=[]; red=[] 
    
    bipartite=True
    
    for v in G.keys(): 
        colour[v]="WHITE"      
    for v in G.keys(): 
        if colour[v]=="WHITE":
            bipartite,colour,red,blue = BFSvisit(G,v,colour,red,blue,bipartite) 
        if bipartite==False: 
            return bipartite,red,blue
                 
    return bipartite,red,blue 

def BFSvisit(G,node,colour,red,blue,bipartite):
    
    d={};queue=[]
    colour[node]="GREY"; d[node]=0 
    
    queue.insert(0,node)    
   
    while queue:
        
        u=queue[len(queue)-1]
       
        for v in G[u]:
            if colour[v]=="WHITE": 
                colour[v]="GREY"; d[v]=d[u]+1   
                queue.insert(0,v)
            elif colour[v]=="GREY":
                if d[u]==d[v]:                
                    bipartite=False 
                    return bipartite,colour,red,blue                   
   
        queue.pop()     
        colour[u]="BLACK"
        if d[u] % 2==0: 
            red.append(u)
        else: 
            blue.append(u) 
    
    return bipartite,colour,red,blue             

def main():
    
    G1 = {0:[4,5],1:[4,5],2:[5],3:[5],4:[0,1],5:[0,1,2,3],
      6:[]}

    G2 = {0:[4,5],1:[4,5],2:[5],3:[5,6],4:[0,1],5:[0,1,2,3],
      6:[3]}

    G3 = {0:[1,2,3],1:[0,2,3],2:[0,1,3],3:[0,1,2],4:[5],5:[4]} 

    
    G4 = {0:[1,2,3],1:[2,0],2:[0,1,3],3:[0,2]}
    
    print("For graph G1:") 
    
    bipartite, red, blue = Bipartition(G1)
    
    if bipartite: 
        print("red:",red,"blue:",blue)
    else:
        print("The graph is not bipartite.")
   

    print("For graph G2:") 
        
    bipartite, red, blue = Bipartition(G2)

    if bipartite: 
        print("red:",red,"blue:",blue)
    else:
        print("The graph is not bipartite.")
   
    print("For graph G3:") 
            
    bipartite, red, blue = Bipartition(G3)
    
    if bipartite: 
        print("red:",red,"blue:",blue)
    else:
        print("The graph is not bipartite.")    
    
    print("For graph G4:") 
                
    bipartite, red, blue = Bipartition(G4)
        
    if bipartite:         
        print("red:",red,"blue:",blue)
    else:
        print("The graph is not bipartite.")  

main()    