class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        for i in range(len(nums)-slow):
            nums[slow]=0
            slow+=1
        return nums



        