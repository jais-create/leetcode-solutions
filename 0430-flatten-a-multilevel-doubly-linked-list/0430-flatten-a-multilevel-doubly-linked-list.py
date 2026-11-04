"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        while curr:
            if curr.child:
                temp=curr.next
                c=curr.child
                curr.next=c
                c.prev=curr
                curr.child=None
                tail=c
                while tail and tail.next:
                    tail=tail.next
                tail.next=temp
                if temp:
                    temp.prev=tail
            curr=curr.next
        return head






         
            







        