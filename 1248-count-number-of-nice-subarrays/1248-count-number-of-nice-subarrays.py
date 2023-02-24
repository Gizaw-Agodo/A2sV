class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] = nums[i]%2
        
        dic = defaultdict(int)
        count = 0
        cursum = 0
        
        for n in nums :
            cursum +=n
            if cursum == k :
                count +=1
            if cursum-k in dic :
                count += dic[cursum-k]
            dic[cursum] += 1
        return count
        

       
            
                
                