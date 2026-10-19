# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1=list1
        ans=curr1
        c=1
        while curr1 and curr1.next:
            
            if c==a:
                temp=curr1.next
                curr1.next=list2
                while temp and temp.next and b!=c:
                    temp=temp.next
                    c+=1
                while curr1 and curr1.next:
                    curr1=curr1.next
                curr1.next=temp.next
            c+=1
            curr1=curr1.next
        return ans

            

        