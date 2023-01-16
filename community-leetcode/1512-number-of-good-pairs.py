class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        answer = 0
        for num in nums:
            answer += count[num] -1
            count[num]-=1
        return answer
