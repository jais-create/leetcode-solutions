class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow=1
        fast=1
        c=1
        while fast!=len(nums):
            if nums[fast]==nums[fast-1]:
                c+=1
            else:
                c=1
            if c<=2:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow





        