class Node:
    
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def setNext(self,newnext):
        self.next = newnext
         

class LinkedList:

    def __init__(self):
        self.head = None  
        self.pointer = None    
    
    def attach_node_to_pointer(self,newnode):   
        if self.head==None: 
            self.head=newnode
            self.pointer=newnode 
        else:    
            self.pointer.setNext(newnode)
            self.pointer=newnode
         
    def removehead(self):        # works only for a nonempty list
        self.head=self.head.next
        

def create_list_from_head(a): 
    mylist=LinkedList()
    if len(a)>0:
        for i in range(0,len(a)):
            mylist.attach_node_to_pointer(Node(a[i]))
    return mylist
    
def printlist(mylist):
    p=mylist.head
    while p!=None:
        print(p.data)  
        p=p.next


def mergelists(list1,list2): 
    
    newlist=LinkedList() 
   
    while list1.head!=None and list2.head!=None: 
        
        if list1.head.data<=list2.head.data:
            newlist.attach_node_to_pointer(list1.head)
            list1.removehead()
        else:     
            newlist.attach_node_to_pointer(list2.head)
            list2.removehead() 
    
    if list1.head==None: 
        newlist.attach_node_to_pointer(list2.head)
    else: 
        newlist.attach_node_to_pointer(list1.head)

    return newlist

list1=create_list_from_head([3,4,6])
list2=create_list_from_head([1,4,5,7])

printlist(mergelists(list1,list2))

