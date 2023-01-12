class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = set()
        count = 0
    
        for i in range(1,len(strs)):
            for j in range(len(strs[i])):
                if strs[i][j] < strs[i-1][j] and j not in deleted:
                    deleted.add(j)
                    count +=1
        return count
                
            