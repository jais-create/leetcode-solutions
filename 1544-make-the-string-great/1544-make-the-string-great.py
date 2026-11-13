class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]

        for i in range(len(s)):
            if len(stack)!=0 and s[i].isupper() and stack[-1]==s[i].lower():
                stack.pop()
            elif len(stack)!=0 and s[i].islower() and stack[-1]==s[i].upper():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
        