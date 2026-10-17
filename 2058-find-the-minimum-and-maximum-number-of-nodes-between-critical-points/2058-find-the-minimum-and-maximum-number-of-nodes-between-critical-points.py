# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        arr=[]
        ind=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        if len(arr)==1 or len(arr)==2:
            return[-1,-1]
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                ind.append(i)
            if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                ind.append(i)
        if len(ind)<2:
            return[-1,-1]
        res=[]
        mn=99999999
        res.append(ind[len(ind)-1]-ind[0])
        for i in range(len(ind)-1):
            mn=min(mn,ind[i+1]-ind[i])
        res.append(mn)

        return sorted(res)
        


        