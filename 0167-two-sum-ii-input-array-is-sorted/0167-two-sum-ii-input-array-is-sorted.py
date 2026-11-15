class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left=0
        right=len(nums)-1
        while right>left:
            if nums[right]+nums[left]==target:
                return[left+1,right+1]
            elif nums[right]+nums[left]>target:
                right-=1
            else:
                left+=1

        