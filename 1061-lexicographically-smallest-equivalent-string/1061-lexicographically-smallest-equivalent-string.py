class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = defaultdict()
        for letter in s1:
            parent[letter] = letter
        for letter in s2:
            parent[letter] = letter
        
        def find(x):
            if x != parent[x] :
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot = find(x)
            yroot = find(y)
            
            if xroot <= yroot:
                parent[yroot] = xroot
            else:
                parent[xroot] = yroot
        
        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        answer = ''
       
        for letter in baseStr:
           
            if letter not in parent:
                answer += letter
            else:
                value = find(letter)
                answer += value
        return answer
                
        