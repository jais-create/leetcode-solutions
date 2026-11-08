class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer=prices.copy()
        stack=[]
        for i in range(len(prices)):
            while stack and prices[i]<=prices[stack[-1]]:
                popped_indx=stack.pop()
                answer[popped_indx]=prices[popped_indx]-prices[i]
            stack.append(i)
        return answer