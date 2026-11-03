# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False
        curr=head
        freq={}
        while curr:
            if curr in freq:
                return True
            else:
                freq[curr]=0
            curr=curr.next
        return False
            
