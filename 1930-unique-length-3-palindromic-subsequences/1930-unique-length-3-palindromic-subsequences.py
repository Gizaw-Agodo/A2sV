class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_dic = defaultdict(int)
        last_dic = defaultdict(int)
        visited = []
        count = 0
        for i in range(len(s)-1,-1,-1):
            first_dic[s[i]] = i
            
        for i in range(len(s)):
            last_dic[s[i]] = i
        
        for i in range(len(s)):
            if s[i] not in visited:
                count += len(set(s[first_dic[s[i]]+1:last_dic[s[i]]]))
                visited.append(s[i])
        return count