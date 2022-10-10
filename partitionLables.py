class Solution:
    def partitionLabels(self, s: str) -> List[int]:
     
        n = len(s)
        dic = defaultdict(int)
        ans = []
        for i in range(n):
            dic[s[i]] = i 
        
        begin,end = 0,0
        ans = []
        
        for i in range(n):
            end = max(end,dic[s[i]])
            
            if i == end :
                ans.append(end-begin +1)
                begin = end +1
                
                
        return ans
