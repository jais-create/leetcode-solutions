# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head==None or head.next==None:
            return head
        
        curr=head
        while curr and curr.next:
            if curr.val==curr.next.val:
                if curr.next.next:
                    curr.next=curr.next.next
                else:
                    curr.next=None
            else:
                curr=curr.next
        return head


        