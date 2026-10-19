# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            new_node=curr.next
            curr.next=prev
            prev=curr
            curr=new_node
        temp=None
        c=0
        while prev:
            
            n=prev.val*2+c
            c=n//10
            new=ListNode(n%10)
            new.next=temp
            temp=new
            prev=prev.next
        
        if c!=0:
            extra=ListNode(c)
            extra.next=temp
            return extra
        else:
            return temp


        
        