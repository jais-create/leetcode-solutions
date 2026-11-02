# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        first=arr[k-1]
        last=arr[len(arr)-k]
        arr[k-1],arr[len(arr)-k]=last,first
        new=ListNode()
        newh=new
        for i in range(len(arr)):
            new.next=ListNode(arr[i])
            new=new.next
        return newh.next



        

        
        

        