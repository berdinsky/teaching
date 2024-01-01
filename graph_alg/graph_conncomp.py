def DFS(G): 
    colour={} # pred={}; seen={}; done={}
    number=0
    for i in G.keys(): 
        colour[i]="WHITE"  
       
    for i in G.keys(): 
        if colour[i]=="WHITE":
            number=number+1
            DFSvisit(G,i,colour,number)
    
def DFSvisit(G,node,colour,number):
    stack=[]
    colour[node]="GREY"
    
    stack.append(node)
    
    print('The nodes of a component N ',number,':')  # printing node
    print(node,' ')    
   
    while stack:
        
        u=stack[len(stack)-1]
       
        whitenbr=False
        for i in G[u]:
            if colour[i]=="WHITE": 
                whitenbr=True  
                v=i
                break
        
        if whitenbr==True:    
            colour[v]="GREY"
           
            stack.append(v)          
             
            print(v)  # printing node
        
        else: 
            stack.pop()
            colour[u]="BLACK"
            
    return colour            
def main():
    
    G = {0:[1,3],1:[0,3],3:[0,1],2:[4,5],4:[2,5],5:[2,4]}

   
    DFS(G)
    
    
main()    