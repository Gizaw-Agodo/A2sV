class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dic = defaultdict(int)
        max_count = 0
        left = 0
        for right in range(len(s)):
            count_dic[s[right]] += 1
            while (right-left + 1) - max(count_dic.values()) > k:
                count_dic[s[left]] -= 1
                left += 1
            max_count = max(max_count , (right-left+1))
        return max_count
            

          
                