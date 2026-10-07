class Solution:
    def isPalindrome(self, x: int) -> bool:
        if "-" in str(x):
            return False
        no=x
        rev=0
        while no:
            dig=no%10
            rev=rev*10+dig
            no=no//10
        if x==rev:
            return True

        return False



        