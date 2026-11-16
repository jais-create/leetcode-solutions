class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        maxx=0
        right=len(height)-1
        while right>left:
            if height[right]>height[left]:
                maxx=max(maxx,min(height[right],height[left])*(right-left))
                left+=1
            else:
                maxx=max(maxx,min(height[left],height[right])*(right-left))
                right-=1
        return maxx
  

        