# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        curr=head
        sum=0
        c=0
        while curr:
            c+=1
            curr=curr.next
        n=c//2
        prev=None
        curr=head
        while curr and n:
            curr=curr.next
            n-=1

        while curr:
            new_node=curr.next
            curr.next=prev
            prev=curr
            curr=new_node
            
        curr=head
        while prev and curr:
            sum=max(sum,prev.val+curr.val)
            curr=curr.next
            prev=prev.next
        return sum
