class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] = i
        
        ans = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end,dic[s[i]])
            if i == end :
                print("case")
                ans.append(end - start  +1)
                start = i +1
         
        return ans  