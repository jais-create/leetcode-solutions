class Solution:
    def defangIPaddr(self, address: str) -> str:
        newadd=""
        for s in address:
            if s is ".":
                newadd+="[.]"
            else:
                newadd+=s
        return newadd

        