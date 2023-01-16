class Solution(object):
    def maxOperations(self, nums, k):
        hash = defaultdict(int)
        cnt = 0 
        
        for num in nums:
            target = k - num
            
            if hash[target] > 0:
                hash[target] -= 1
                cnt += 1
            else:
                hash[num] += 1
                
        return cnt 
