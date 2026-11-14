class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while len(stack) > 0 and num > stack[-1]:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            stack.append(num)
            
        # Phase 2: Build the answer list for nums1 using a regular loop
        answer = []
        for num in nums1:
            if num in next_greater:
                answer.append(next_greater[num])
            else:
                answer.append(-1)
                
        return answer
        