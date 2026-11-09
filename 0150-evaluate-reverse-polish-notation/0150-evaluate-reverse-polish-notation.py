class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        sign="+-*/"
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] in sign:
                b=stack.pop()
                a=stack.pop()
                if tokens[i]=="+":
                    c=a+b
                    stack.append(c)
                if tokens[i]=="-":
                    c=a-b
                    stack.append(c)
                if tokens[i]=="*":
                    c=a*b
                    stack.append(c)
                if tokens[i]=="/":
                    c=int(a/b)
                    stack.append(c)
            else:
                stack.append(int(tokens[i])) 
        return stack[-1]      