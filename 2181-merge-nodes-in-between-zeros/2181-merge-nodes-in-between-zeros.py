# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        arr1=[]
        arr2=[]
        curr=head
        while curr:
            arr1.append(curr.val)
            curr=curr.next
        total=0
        for i in range(1,len(arr1)):
            if arr1[i] !=0:
                total+=arr1[i]
            else:
                arr2.append(total)
                total=0
        new=ListNode()
        ret=new
        for i in range(len(arr2)):
            new.val=arr2[i]
            if i+1<len(arr2):
                new.next=ListNode(arr2[i+1])
            else:
                new.next=None
            new=new.next
        return ret



        