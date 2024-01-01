class TreeNode:
   
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor=0

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
                    currentNode.leftChild = TreeNode(key,val,
                                                     parent=currentNode)
                    self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                    self._put(key,val,currentNode.rightChild)
            else:
                    currentNode.rightChild = TreeNode(key,val,
                                                      parent=currentNode)
                    self.updateBalance(currentNode.rightChild)
    
    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                    node.parent.balanceFactor += 1
            elif node.isRightChild():
                    node.parent.balanceFactor -= 1
    
            if node.parent.balanceFactor != 0:
                    self.updateBalance(node.parent)    
    
    def isRoot(self,node): 
        return self.root==node
    
    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if self.isRoot(rotRoot):
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                    rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
                                       newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
                                       rotRoot.balanceFactor, 0)    
    
    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if self.isRoot(rotRoot):
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                    rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(
                                       newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(
                                       rotRoot.balanceFactor, 0)    
    
    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)    
   
     
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
    
    def _printBST(self,current,*leftnotright):
        
        if self.root != current:  
            if leftnotright[0]: 
                print(" P",current.parent.key,"L",current.payload,end="|")
            else: 
                print(" P",current.parent.key,"R",current.payload,end="|")
        else: 
            print("ROOT",current.payload,end="|") 
        
        if current.hasLeftChild():
            self._printBST(current.leftChild,True)
        if current.hasRightChild(): 
            self._printBST(current.rightChild,False)     
    
   
def main(): 
    
    adict={} # creating a dictionary
                
    BST=BinarySearchTree()     
                
    BST.buildup(adict)   
    
    for i in range(20): 
    
        print('\nAdd Key=',i,',Value=',i); BST.put(i,i)
    
        BST.printBST()    
    
main()    