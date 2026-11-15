class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        greater={}
        stack=[]
        answer=[]
        for i in range(len(nums2)):
            while stack and  nums2[i]>stack[-1]:
                popp=stack.pop()
                greater[popp]=nums2[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] in greater:
                answer.append(greater[nums1[i]])
            else:
                answer.append(-1)
        return answer







        