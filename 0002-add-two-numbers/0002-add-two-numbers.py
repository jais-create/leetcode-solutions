# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if l1==None and l2==None:
            return None
        carry=0
        ans=None
        ansh=ans
        while l1 or l2:
            add=0
            if l1==None:
                val1=0
            else:
                val1=l1.val
            if l2==None:
                val2=0
            else:
                val2=l2.val
            add=val1+val2+carry
            carry=add//10
            if ansh==None:
                ans = ListNode(add % 10)
                ansh = ans
            else:
                ans.next=ListNode(add%10)
                ans=ans.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            ans.next = ListNode(carry)
        return ansh







        
        