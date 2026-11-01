# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next==None:
            return False
        freq={}
        curr=head
        while curr:
            if curr not in freq:
                freq[curr]=1
                curr=curr.next
            else:
                return True
        return False
