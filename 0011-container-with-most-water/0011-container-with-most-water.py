class Solution:
    def maxArea(self, height: list[int]) -> int:
        st=0
        maxx=0
        last=len(height)-1
        while last>st:
            if height[last]>height[st]:
                maxx=max(maxx,(last-st)*min(height[last],height[st]))
                st+=1
            else:
                maxx=max(maxx,(last-st)*min(height[last],height[st]))
                last-=1
        return maxx

        