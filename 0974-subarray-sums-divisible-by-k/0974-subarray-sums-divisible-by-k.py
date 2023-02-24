class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_dic = defaultdict(int)
        pref_sum = 0
        count = 0
        for num in nums:
            pref_sum += num
            remainder = pref_sum % k
            if remainder  == 0:
                count += 1
            if remainder in rem_dic:
                count += rem_dic[remainder]
            rem_dic[remainder] += 1
        return count
            