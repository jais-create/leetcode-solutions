# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next==None:
            return None
        
        slow=head
        fast=head
        n=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            n+=1
        curr=head
        ans=curr
        while curr and curr.next:
            if curr.next.val==slow.val and n==1:
                curr.next=curr.next.next
                break
            n-=1
            curr=curr.next
        return ans


        