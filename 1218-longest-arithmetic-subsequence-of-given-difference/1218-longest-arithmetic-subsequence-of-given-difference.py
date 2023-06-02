class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)
        answer = float('-inf')
        for num in arr:
            curr_val = memo[num-difference] + 1
            memo[num] = curr_val
            answer = max(answer, memo[num])
        return answer
            