class Solution:
    def reverseVowels(self, s: str) -> str:
        vow="aeiouAEIOU"
        start=0
        end=len(s)-1
        s=list(s)
        while start<end:
            if s[start] in vow and s[end] in vow:
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1
            elif s[start] in vow and s[end] not in vow:
                end-=1
            elif s[start] not in vow and s[end] in vow:
                start+=1
            else:
                start+=1
                end-=1
        s="".join(s)
        return s




        