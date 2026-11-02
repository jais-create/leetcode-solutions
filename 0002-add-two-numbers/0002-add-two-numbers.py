# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if l1==None and l2==None:
            return None
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 :
            sum=0
            if l1 and l2:
                sum=l1.val+l2.val+carry
            if l1 and l2==None:
                sum=l1.val+carry
            if l2 and l1==None:
                sum=l2.val+carry
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

            new=ListNode(sum%10)
            carry=sum//10
            dummy.next=new
            dummy=dummy.next
        if carry:
            dummy.next=ListNode(carry)
            dummy=dummy.next
        return curr.next
                








        
        