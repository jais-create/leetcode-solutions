class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[-1]*len(nums1)
        stack=[]
        greater={}
        for i in range(len(nums2)):
            if stack and nums2[i]>nums2[stack[-1]]:
                popp=stack.pop()
                greater[nums2[popp]]=nums2[i]
            stack.append(i)
        for i in range(len(nums1)):
            if nums1[i] in greater:
                ans[i]=greater[nums1[i]]
        return ans














        