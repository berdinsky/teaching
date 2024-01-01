# first step: ordering nodes and reversing a digraph 

def Reverse(G):  # here we reverse a digraph 
    H={}
    for i in G.keys():
        H[i]=[]
    for i in G.keys(): 
        for j in G[i]:
            H[j].append(i) 
    return H

def DFS(G): 
    colour={}; done=[]
    for i in G.keys(): 
        colour[i]="WHITE"      
    for i in G.keys(): 
        if colour[i]=="WHITE":
            colour,done = DFSvisit(G,i,colour,done)
    return done
    

def DFSvisit(G,node,colour,done):
    stack=[]
    colour[node]="GREY"  
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
            colour[v]="GREY"
            stack.append(v)
                   
        else: 
            stack.pop()
            colour[u]="BLACK"; done.append(u)
    
    return colour,done 

# second step: finding strong connected components 
 
def DFS2(G,done): 
    colour={} 
    number=0
    for i in G.keys(): 
        colour[i]="WHITE"  
       
    for i in range(len(done)): 
        if colour[done[i]]=="WHITE":
            number=number+1
            DFSvisit2(G,done[i],colour,number)
    
def DFSvisit2(G,node,colour,number):
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
    
    # Test 1 

    G = {0:[1,3],1:[2],2:[0],3:[]}

    print("For graph:", G) 
    
    done = DFS(G); done.reverse() 
    H = Reverse(G); DFS2(H,done) 

    # Test 2 

    G = {0:[1,3],1:[],2:[0],3:[1,2],4:[2,3,5],5:[3,4]}

    print("For graph:", G) 
    
    done = DFS(G); done.reverse() 
    H = Reverse(G); DFS2(H,done) 


main()               