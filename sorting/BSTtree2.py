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
    
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)    
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self    
    
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild    
    
    def hasBothChildren(self):
        return self.rightChild and self.leftChild  
    
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self    
    
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
    
    def findSuccessor(self,currentNode):
        succ = None
        if currentNode.hasRightChild():
            succ = self.findMin(currentNode.rightChild)
        else:
            if currentNode.parent:
                if currentNode.isLeftChild():
                    succ = currentNode.parent
                else:
                    currentNode.parent.rightChild = None
                    succ = currentNode.parent.findSuccessor()
                    currentNode.parent.rightChild = currentNode
        return succ
    
    def findMin(self,currentNode):
        current = currentNode
        while current.hasLeftChild():
            current = current.leftChild
        return current    
    
    def spliceOut(self,currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasAnyChildren():
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.leftChild
                else:
                    currentNode.parent.rightChild = currentNode.leftChild
                currentNode.leftChild.parent = currentNode.parent
            else:
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.rightChild
                else:
                    currentNode.parent.rightChild = currentNode.rightChild
                currentNode.rightChild.parent = currentNode.parent      
               
    
    def remove(self,currentNode):   
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
                
        elif currentNode.hasAnyChildren() and not currentNode.hasBothChildren(): # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                    currentNode.leftChild.payload,
                    currentNode.leftChild.leftChild,
                    currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                    currentNode.rightChild.payload,
                    currentNode.rightChild.leftChild,
                    currentNode.rightChild.rightChild)    
                
        else:  # this node has both children  
            succ = self.findSuccessor(currentNode)    
            self.spliceOut(succ)
            currentNode.key = succ.key
            currentNode.payload = succ.payload  
            
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')            
    
  
        
def main(): 
    
    adict={17:'17',5:'5',2:'2',16:'16',
           35:'35',29:'29',33:'33',
           38:'38'} # creating a dictionary
                
    BST=BinarySearchTree()     
                
    BST.buildup(adict)        
    
    BST.printBST()
    
    print('')
    print('Delete 17 and add 19.')
    
    BST.delete(17); BST.put(19,'19')
    
    BST.printBST()
    

main() 