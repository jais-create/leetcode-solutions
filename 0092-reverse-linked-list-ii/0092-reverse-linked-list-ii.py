# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head==None or left==right:
            return head
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        for i in range(left-1):
            prev=prev.next
        curr=prev.next
        for i in range(right-left):
            temp=curr.next
            curr.next=temp.next
            temp.next=prev.next
            prev.next=temp
        return dummy.next










        