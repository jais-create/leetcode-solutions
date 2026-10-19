# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1==None and list2==None:
            return None
        if list1==None and list2!=None:
            return list2
        if list2==None and list1!=None:
            return list1
        dummy=ListNode()
        curr=dummy
        while list1 and list2:
            if list1.val>list2.val:
                dummy.next=list2
                list2=list2.next
            else:
                dummy.next=list1
                list1=list1.next
                
            dummy=dummy.next
        if list1:
            dummy.next=list1
        if list2:
            dummy.next=list2
        return curr.next
        