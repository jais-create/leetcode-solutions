class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer=[0]*(len(temperatures))
        stack=[]
      
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                popped_indx=stack.pop()
                answer[popped_indx]=i-popped_indx
            stack.append(i)
        return answer
        