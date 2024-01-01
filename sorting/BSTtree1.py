# this program creates a BST from a dictionary and returns  
# the value for a given key  
   
class TreeNode:
   
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1
    
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)   


    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
     
    def buildup(self,adict): 
        print('The order in which elements are added to BST:')
        for key,val in adict.items():
            print(key,end=" ")
            self.put(key,val)  
        print('')
    
    def printBST(self): 
        
        print('Print out the elements of BST:')
        if self.root: 
            self._printBST(self.root)
        else: 
            print('The Binary Search Tree is empty')
    
    def _printBST(self,current):
        print(current.payload,end=" ") 
        if current.hasLeftChild():
            self._printBST(current.leftChild)
        if current.hasRightChild(): 
            self._printBST(current.rightChild)     

def main(): 
    adict={17:'17',5:'5',2:'2',16:'16',
           35:'35',29:'29',33:'33',38:'38'} # creating a dictionary
    
    BST=BinarySearchTree()     
    
    BST.buildup(adict)       
    
    BST.printBST()
    
    print('\nAdd the element Key=1,Val=1.') 
    
    BST.put(1,'1')
    
    BST.printBST()
    
    print('\nGet the value of the key 33:',BST.get(33))
                   
main() 