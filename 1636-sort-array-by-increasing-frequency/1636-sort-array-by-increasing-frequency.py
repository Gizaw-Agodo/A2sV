class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        count_list = [[k, v] for k, v in count.items()]
        count = sorted(count_list, key = lambda x: (x[1], -x[0]))
        ans = []
        for key,val in count :
            ans += [key]*val
        return ans
