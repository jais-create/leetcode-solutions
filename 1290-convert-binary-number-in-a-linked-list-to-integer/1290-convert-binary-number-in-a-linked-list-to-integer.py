# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        curr=head
        c=0
        no=0
        while curr and curr.next:
            curr=curr.next
            c+=1
        curr=head
        while curr:
            no+=curr.val*2**c
            c=c-1
            curr=curr.next
        return no  
        