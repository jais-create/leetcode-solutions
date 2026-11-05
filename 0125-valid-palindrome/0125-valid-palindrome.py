class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st=0
        last=len(s)-1
        while last>st:
            if s[st].isalnum() and s[last].isalnum():
                if s[st]==s[last]:
                    st+=1
                    last-=1
                else:
                    return False
            while s[last].isalnum()==False and last>0:
                last-=1
            while s[st].isalnum()==False and st<last:
                st+=1
        return True
            

        