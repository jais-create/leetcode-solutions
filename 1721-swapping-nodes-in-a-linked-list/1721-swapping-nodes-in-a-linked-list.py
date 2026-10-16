# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        f=arr[k-1]
        ind=arr[-k]
        arr[k-1],arr[-k]=ind,f
        new=ListNode()
        ret=new
        for i in range(len(arr)):
            new.val=arr[i]
            if i+1<len(arr):
                new.next=ListNode(arr[i+1])
            else:
                new.next=None
            new=new.next
        return ret

        
        

        