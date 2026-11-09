class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxx=0
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                maxx=max(maxx,c)
            if nums[i]==0:
                c=0
        return maxx
        