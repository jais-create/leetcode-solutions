class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer=[]
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            right=len(nums)-1
            left=i+1
            while right>left:
                if nums[i]+nums[left]+nums[right]==0:
                    answer.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[right]+nums[i]+nums[left]<0:
                    left+=1
                else:
                    right-=1

        
        return answer           
