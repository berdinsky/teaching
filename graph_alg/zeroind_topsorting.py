def seeksource(G): 
    for u in G.keys(): 
        source=True
        for v in G.keys():
            if u in G[v]: 
                source=False
        if source:
            return u

def sorting(G): 
    while G:
        u=seeksource(G)
        print(u)
        del G[u] 
    

def main():
    
    G1 = {0:[1,2],1:[3,4],2:[3,4],3:[],4:[]}

    G2 = {0:[1],1:[2,3],2:[4,5],3:[],4:[],5:[]}
    
    print('For G1:')
    sorting(G1)
    print('For G2')
    sorting(G2)
    
main()    