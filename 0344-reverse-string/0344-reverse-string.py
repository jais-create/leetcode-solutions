class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st=0
        l=len(s)-1
        while l>st:
            s[st],s[l]=s[l],s[st]
            st+=1
            l-=1
        return s
        