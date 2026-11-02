# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        curr=head
        while curr and curr.next:
            n=ListNode(math.gcd(curr.val,curr.next.val))
            save=curr.next
            curr.next=n
            n.next=save
            curr=curr.next.next
        return head



        