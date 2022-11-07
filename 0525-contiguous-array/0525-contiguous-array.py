class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        prefsum  = 0
        maxlen = 0
        for i in range ( len(nums)):
            if nums[i] == 1:
                prefsum += nums[i] 
            else: 
                prefsum -=1 
            
            if  prefsum in dic :
                maxlen = max(maxlen,i-dic[prefsum])
            else:
                dic[prefsum] = i
        return maxlen
            
                
                
            
            
            