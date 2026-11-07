class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open="({["
        clos=")}]"
        c=0
        if s[0] in clos:
            return False
        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
                c+=1
            if s[i] in clos and len(stack)!=0:
                if stack[-1]=="(" and s[i]==")" or stack[-1]=="[" and s[i]=="]" or stack[-1]=="{" and s[i]=="}":
                    stack.pop()
                    c+=1
                else:
                    return False
        if c-1!=i:
            return False
            
        if len(stack)==0:
            return True
        else:
            return False


        