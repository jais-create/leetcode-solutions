class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer=[0]*(len(temperatures))
        stack=[]
        for i in range (len(temperatures)):
            while len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]:
                popp=stack.pop()
                answer[popp]=i-popp
            stack.append(i)


        return answer

            
        