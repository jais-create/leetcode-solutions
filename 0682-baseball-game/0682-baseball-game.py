class Solution:
    def calPoints(self, ops: list[str]) -> int:
        stack=[]
        sum=0
        oper="+DC"
        for i in range(len(ops)):
            if len(stack)!=0 and ops[i] in oper:
                if ops[i]=="+":
                    temp=int(stack[-1])+int(stack[-2])
                    stack.append(temp)
                elif ops[i]=="D":
                    temp=int(stack[-1])*2
                    stack.append(temp)
                elif ops[i]=="C":
                    stack.pop()
            else:
                stack.append(int(ops[i]))
   
        for i in range(len(stack)):
            sum+=stack[i]
        return sum
