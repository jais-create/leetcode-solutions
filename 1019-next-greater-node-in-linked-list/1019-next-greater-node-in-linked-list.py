# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        ans = [0] * len(arr)
        stack = []

        for i, val in enumerate(arr):
            while stack and val > arr[stack[-1]]:
                idx = stack.pop()
                ans[idx] = val

            stack.append(i)

        return ans



        