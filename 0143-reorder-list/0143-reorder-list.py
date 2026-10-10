# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return head
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        nxt=slow.next
        slow.next=None
        prev2=None
        curr2=nxt
        while curr2:
            new_node=curr2.next
            curr2.next=prev2
            prev2=curr2
            curr2=new_node
        curr1=head
        while curr1 and prev2:
            save1=curr1.next
            curr1.next=prev2
            save2=prev2.next
            prev2.next = save1
            curr1=save1
            prev2=save2
        return head

        