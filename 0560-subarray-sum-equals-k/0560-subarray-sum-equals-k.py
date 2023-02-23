class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        count = 0
        cursum = 0
        for n in nums :
            cursum +=n
            if cursum == k :
                count +=1
            if cursum-k in dic :
                count += dic[cursum-k]
            dic[cursum] +=1
        return count
                    
            