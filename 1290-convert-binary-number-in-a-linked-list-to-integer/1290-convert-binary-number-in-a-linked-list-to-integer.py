# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        curr=head
        c=0
        ans=0
        while curr and curr.next:
            c+=1
            curr=curr.next
        curr=head
        while curr:
            ans+=2**c*curr.val
            c-=1
            curr=curr.next
        return ans
