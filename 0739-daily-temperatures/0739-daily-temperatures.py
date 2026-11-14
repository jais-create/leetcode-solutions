class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        answer=[0]*(len(temp))
        stack=[]
        for i in range(len(temp)):
            while stack and temp[stack[-1]]<temp[i]:
                popp=stack.pop()
                answer[popp]=i-popp
            else:
                stack.append(i)
        return answer

            
        