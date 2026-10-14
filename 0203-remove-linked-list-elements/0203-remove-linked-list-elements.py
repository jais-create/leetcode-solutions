# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        curr=head
        if head is None:
            return None
        while head and head.val==val:
            head=head.next
        while curr and curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
        