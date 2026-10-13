class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class MyLinkedList:

    def __init__(self):
        self.head=None
    def get(self, index: int) -> int:
        curr=self.head
        c=0
        while curr:
            if c==index:
                return curr.data
            c+=1
            curr=curr.next
        if curr==None:
            return -1
    def addAtHead(self, val: int) -> None:
        new=Node(val)
        new.next=self.head
        if self.head:
            self.head.prev=new
        self.head=new

    def addAtTail(self, val: int) -> None:
        last=Node(val)
        if self.head==None:
            self.head=last
            return
        
        curr=self.head
        while curr and curr.next:
            curr=curr.next
        curr.next=last
        last.prev=curr
    def addAtIndex(self, index: int, val: int) -> None:
        new=Node(val)
        if index==0:
            self.addAtHead(val)
            return
        c=1
        curr=self.head
        while curr:
            if index==c:
                new.next=curr.next
                new.prev=curr
                if curr.next:
                    curr.next.prev=new
                curr.next = new
            c+=1
            curr=curr.next
        return
    def deleteAtIndex(self, index: int) -> None:
        if self.head==None:
            return
        if index==0:
            self.head=self.head.next
        
            if self.head:
                self.head.prev=None
            return
        c=1
        curr=self.head.next
        while curr:
            if index==c:
                curr.prev.next=curr.next
                if curr.next:
                    curr.next.prev=curr.prev
                return
            c+=1
            curr=curr.next
        return

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)