# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        if head==None or head.next==None or head.next.next==None:
            return[-1,-1]
        arr=[]
        indx=[]
        ans=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                indx.append(i+1)
            if arr[i-1]>arr[i] and arr[i+1]>arr[i]:
                indx.append(i+1)
        if len(indx)<2:
            return[-1,-1]
        minn=99999999
        for i in range(len(indx)-1):
            minn=min(minn,indx[i+1]-indx[i])
        max=indx[len(indx)-1]-indx[0]
        ans.append(minn)
        ans.append(max)
        return ans
        

        


        


        