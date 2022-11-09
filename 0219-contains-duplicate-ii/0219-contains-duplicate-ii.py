class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)
        start = 0
        for i in range(len(nums)):
            dic[nums[i]]+=1
            if dic[nums[i]] > 1:
                return True
            if i - start  == k:
                dic[nums[start]]-=1
                start +=1
        return False
                