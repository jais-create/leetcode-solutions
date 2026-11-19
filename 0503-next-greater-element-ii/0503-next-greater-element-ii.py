class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        ans=[-1]*(len(nums))
        stack=[]
        for i in range(len(nums)*2):
            while stack and nums[stack[-1]]<nums[i%len(nums)]:
                ans[stack[-1]]=nums[i%len(nums)]
                stack.pop()
            if i<len(nums):
                stack.append(i%len(nums))
        return ans


        