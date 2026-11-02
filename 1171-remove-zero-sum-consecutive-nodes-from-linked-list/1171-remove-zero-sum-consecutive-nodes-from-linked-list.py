# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head):
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr1 = []
        i = 0

        while i < len(arr):
            total = 0
            j = i

            while j < len(arr):
                total += arr[j]

                if total == 0:
                    break

                j += 1

            if total == 0:
                i = j + 1
            else:
                arr1.append(arr[i])
                i += 1

        new = ListNode(0)
        newh = new

        for x in arr1:
            new.next = ListNode(x)
            new = new.next

        return newh.next
        