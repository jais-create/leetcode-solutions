class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix=[0]*(len(gain)+1)
        prefix[0]=0
        sum=0
        for i in range(len(gain)):
            sum+=gain[i]
            prefix[i+1]=sum
        return max(prefix)
        