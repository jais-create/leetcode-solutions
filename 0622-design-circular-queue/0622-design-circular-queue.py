class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.front = 0
        self.size = 0
    def enQueue(self, value: int) -> bool:
        if self.size<self.k:
            self.queue[(self.front+self.size)%self.k]=value
            self.size+=1
            return True
        return False
    def deQueue(self) -> bool:
        if self.size==0:
            return False
        self.queue[(self.front)]=0
        self.front=(self.front+1)%self.k
        self.size-=1
        return True
    def Front(self) -> int:
        if self.size==0:
            return -1
        return self.queue[self.front]
    def Rear(self) -> int:
        if self.size==0:
            return -1
        return self.queue[(self.size+self.front-1)%self.k]
    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        return False
    def isFull(self) -> bool:
        if self.size==self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()