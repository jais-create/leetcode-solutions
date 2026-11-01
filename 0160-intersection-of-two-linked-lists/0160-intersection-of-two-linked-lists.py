# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        movea=0
        moveb=0
        curr1=headA
        curr2=headB
        while curr1:
            curr1=curr1.next
            movea+=1
        while curr2:
            curr2=curr2.next
            moveb+=1
        curr1=headA
        curr2=headB
        if movea>moveb:
            diff=movea-moveb
            while diff:
                curr1=curr1.next
                diff-=1
        else:
            diff=moveb-movea
            while diff:
                curr2=curr2.next
                diff-=1
        while curr1 and curr2:
            if curr1==curr2:
                return curr1
            curr1=curr1.next
            curr2=curr2.next
        return None


        



        