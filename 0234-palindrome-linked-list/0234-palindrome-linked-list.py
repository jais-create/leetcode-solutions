# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        curr=slow 
        while curr:
            next=curr.next
            curr.next=prev
            prev,curr=curr,next
        temp=head
        while prev:
            if temp.val!=prev.val:
                return False
            prev=prev.next
            temp=temp.next
        return True


            
        
        