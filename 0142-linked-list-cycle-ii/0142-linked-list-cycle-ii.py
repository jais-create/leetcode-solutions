# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq={}
        curr=head
        ptr=None

        while curr:
            if curr in freq:
                return curr
            else:
                freq[curr]=curr
                
            curr=curr.next
        return None

        