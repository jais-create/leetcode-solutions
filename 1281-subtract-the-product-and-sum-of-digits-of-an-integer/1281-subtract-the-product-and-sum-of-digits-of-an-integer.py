class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        sum=0
        res=0
        while n!=0:
            pro*=n%10
            sum+=n%10
            n=n//10
        res=pro-sum
        return res
        
        