class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = list(range(len(strs)))
        rank = [1]*len(strs)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            if rank[par1] >= rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
        
        for i in range(len(strs)):
            word1 = strs[i]
            for j in range(i + 1, len(strs)):
                word2 = strs[j]
                ptr = 0
                count = 0
                while ptr < len(word1):
                    if word1[ptr] != word2[ptr]:
                        count += 1
                    ptr += 1
                if count <= 2:
                    union(i,j)
        
        for i in range(len(strs)):
            find(i)
            
        return len(set(parent))


        
