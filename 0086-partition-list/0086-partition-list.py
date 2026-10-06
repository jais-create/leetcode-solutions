# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if head==None or head.next==None:
            return head
        small=None
        smallh=None
        large=None
        largeh=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=None
            if curr.val<x:
                if small==None:
                    smallh=curr
                    small=curr
                else:
                    small.next=curr
                    small=small.next
            else:
                if large==None:
                    largeh=curr
                    large=curr
                else:
                    large.next=curr
                    large=large.next
            curr=nxt
        if smallh==None:
            return largeh
        if largeh==None:
            return smallh
        else:
            small.next=largeh
            return smallh



