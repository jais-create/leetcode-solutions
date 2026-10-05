class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=[]
        word=s.split()
        return len(word[-1])
        