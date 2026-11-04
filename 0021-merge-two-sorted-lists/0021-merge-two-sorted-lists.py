# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if l1 and l2==None:
            return l1
        if l1==None and l2:
            return l2
        if l1==None and l2==None:
            return None
        dummy=ListNode()
        curr=dummy
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next=l1
                l1=l1.next
                
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        if l1:
            dummy.next=l1
        if l2:
            dummy.next=l2
        return curr.next



        