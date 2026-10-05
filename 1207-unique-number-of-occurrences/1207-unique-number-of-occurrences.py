class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash={}
        seen=set()
        for i in range(len(arr)):
            if arr[i] not in hash:
                hash[arr[i]]=1
            else:
                hash[arr[i]]+=1
        for value in hash.values():
            if value in seen:
                return False
            else:
                seen.add(value)
        return True
       
            