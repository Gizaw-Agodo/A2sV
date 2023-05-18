class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(97 + i): chr(97 + i) for i in range(26)}
        size = {chr(97 + i) :1 for i in range(26)}
      
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
        
        for equation in equations:
            splited = list(equation.strip())
            if equation[1:3] == "==":
                union(splited[0],splited[3])
        
        for equation in equations:
            splited = list(equation.strip())
            if equation[1:3] != "==":
                if find(splited[0]) == find(splited[3]):
                    return False
            
        return True