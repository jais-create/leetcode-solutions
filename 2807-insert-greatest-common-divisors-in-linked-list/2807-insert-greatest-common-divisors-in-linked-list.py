# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        if curr and curr.next==None:
            return curr
        ans=curr
        while curr and curr.next:
            import math
            new=ListNode(math.gcd(curr.val,curr.next.val))
            temp=curr.next
            curr.next=new
            new.next=temp
            curr=curr.next.next
        return ans 


        