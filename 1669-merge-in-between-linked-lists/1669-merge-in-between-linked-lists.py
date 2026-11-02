# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1=list1
        cu=curr1
        c=1
        while curr1:
            if c==a:
                save=curr1.next
                break
            curr1=curr1.next
            c+=1
        curr2=list2
        if curr2:
            curr1.next=curr2
        while curr1 and curr1.next:
            curr1=curr1.next
        iter=b-a
        while iter:
            save=save.next
            iter-=1
        curr1.next=save.next

        return cu



            

        