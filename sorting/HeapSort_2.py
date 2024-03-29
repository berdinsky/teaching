class BinHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2 
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)    
    

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def maxChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i * 2
            else:    
                return i * 2 + 1        
    
    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval           

    def buildHeap(self,alist):
 
        for i in range(len(alist)):
            self.insert(alist[i])
            
     

a=[6,-1,5,7,7,-5,11,-3,-2]

heap=BinHeap() 

heap.buildHeap(a) 

for i in range(len(a)-1,-1,-1): 
    a[i]=heap.delMax()

print(a)




