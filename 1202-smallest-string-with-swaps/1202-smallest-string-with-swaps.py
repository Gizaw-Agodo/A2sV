class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))
        size = [1 for _ in range(len(s))]
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union (x, y):
            xroot = find(x)
            yroot = find(y)
            if size[xroot] >= size[yroot] : 
                parent[yroot] = xroot
                size[xroot] += size[yroot]
            else:
                parent[xroot] = yroot
                size[yroot] += size[xroot]
            
            
        for a,b in pairs:
            union(a,b)
            
        tree = defaultdict(list)
        for i in range(len(s)):
            tree[find(i)].append(s[i])
    
        for key in tree.keys():
            tree[key] = sorted(tree[key], reverse = True)
        
        answer = ""
        for i in range(len(s)):
            root = find(i)
            poped = tree[root].pop()
            answer += poped
            
        return answer