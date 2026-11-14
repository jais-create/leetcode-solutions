class Solution:
    def nextGreaterElement(self, n1: list[int], n2: list[int]) -> list[int]:
        stack=[]
        greater={}
        for n in n2:
            while stack and n>stack[-1]:
                small=stack.pop()
                greater[small]=n
            
            stack.append(n)
        answer=[]
        for i in range(len(n1)):
            if n1[i] in greater:
                answer.append(greater[n1[i]])
            else:
                answer.append(-1)
        return answer




        