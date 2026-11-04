class Node:
    def __init__(self,val=None,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
class MyLinkedList:
    def __init__(self):
        self.head=None
    def get(self, index: int) -> int:
        curr=self.head
        c=0
        while curr:
            if c==index:
                return curr.val
            curr=curr.next
            c+=1
        return -1
    def addAtHead(self, val: int) -> None:
        new=Node(val)
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head.prev=new
            self.head=new
        return

    def addAtTail(self, val: int) -> None:
        new=Node(val)
        if self.head==None:
            self.head=new
            return
        curr=self.head
        while curr and curr.next:
            curr=curr.next
        curr.next=new
        new.prev=curr
        return
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        new = Node(val)
        curr = self.head
        if index == 0:
            self.addAtHead(val)
            return
        c = 0
        while curr and c != index - 1:
            curr = curr.next
            c += 1
        if curr is None:
            return
        save = curr.next
        curr.next = new
        new.prev = curr
        new.next = save
        if save:
            save.prev = new
            return
    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        c = 0
        curr = self.head
        while curr and c != index:
            curr = curr.next
            c += 1
        if curr is None:
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        return

 

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)