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
        curr=slow
        prev=None
        while curr:
            save=curr.next
            curr.next=prev
            prev,curr=curr,save
        curr=head

        temp=prev
        while curr and temp:
            if curr.val!=temp.val:
                return False
            else:
                temp=temp.next
                curr=curr.next
        return True





            
        
        