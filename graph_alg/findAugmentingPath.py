def findAugmentingPath(G,M,x): 
    queue=[]; status=[]; pred=[] 
    for v in G.keys():
        status.append("WHITE") 
        pred.append(None) 
    status[x]="EVEN"     
    queue.insert(0,x) 
    while queue: 
        u=queue.pop()
        if status[u]=="EVEN": 
            for v in G[u]:
                if status[v]=="WHITE":
                    status[v]="ODD"; pred[v]=u
                    if M[v]==None:   # v is not in M                  
                        return pred, v  
                    else: 
                        queue.insert(0,v) 
        else:    
            v=M[u]  # status[u] is EVEN 
            if status[v]=="WHITE": 
                status[v]="EVEN"; pred[v]=u
                queue.insert(0,v) 
    return None    

def print_out_augmenting_path (pred,v):
    print(v)
    t=v
    while pred[t]!=None:
        print(pred[t])
        t=pred[t]


def main(): 
    # A given graph must be bipartite.
    

    # Test 1
    G1={0:[3],1:[3,4,5],2:[4],3:[0],4:[1,2],5:[1]}  # graph
    M=[None]*6
    M[0]=3; M[3]=0; M[1]=4; M[4]=1  # matching
    x=2  # unmatched vertex
    print("The result of Test 1:")
    AugmentingPath = findAugmentingPath(G1,M,x) 
    if AugmentingPath==None:
        print ("There is no augmenting path starting from the vertex",x)
    else: 
        print_out_augmenting_path(AugmentingPath[0],AugmentingPath[1])


    # Test 2
    G2={0:[4,5],1:[5,7],2:[4,6,8],3:[6],4:[0,2],5:[0,1],6:[2,3],7:[1],8:[2]} 
    M=[None]*9
    M[0]=4; M[4]=0; M[1]=5; M[5]=1; M[2]=6; M[6]=2;  # matching
    x=7  # unmatched vertex
    print("The result of Test 2:")
    AugmentingPath = findAugmentingPath(G2,M,x) 
    if AugmentingPath==None:
        print ("There is no augmenting path starting from the vertex",x)
    else: 
        print_out_augmenting_path(AugmentingPath[0],AugmentingPath[1])
main()