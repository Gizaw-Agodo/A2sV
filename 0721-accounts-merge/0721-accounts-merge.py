class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = defaultdict()
        ownership = defaultdict()
        size = defaultdict()
        
        for account in accounts :
            for email in account[1:] :
                parent[email] = email
                ownership[email] = account[0]
                size[email] = 1
                
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot = find(x)
            yroot = find(y)
            
            if size[xroot] >= size[yroot]:
                parent[yroot] = xroot
                size[xroot] += size[yroot]
            else:
                parent[xroot] = yroot
                size[yroot] += size[xroot]
        
        for account in accounts :
            owner = account [0]
            for i in range(1,len(account)):    
                union(account[1] , account[i])
        
        tree = defaultdict(list)
        for item in parent.keys():
           
            root = find(item)
            tree[root].append(item)
        
        answer = []
        for root in tree.keys():
            owner = ownership[root]
            answer.append([owner] + sorted(tree[root]))
                          
        return answer
            
            