class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        maxx=0
        sum=0
        for i in range(k):
            sum+=nums[i]
        maxx=sum
        for i in range(1,len(nums)-k+1):
            sum=sum-nums[i-1]+nums[i+k-1]
            maxx=max(maxx,sum)
        return maxx/k