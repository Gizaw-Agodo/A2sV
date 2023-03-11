class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key in count :
            if count[key] > len(nums)//2:
                return key
        