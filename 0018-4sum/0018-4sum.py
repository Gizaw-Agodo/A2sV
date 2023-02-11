class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        fourSum = []
        nums.sort()
        if n < 4 :
            return []
        for i in range(n):
            for j in range(i+1,n):
                start , end = j+1,n-1
                while start < end :
                    currSum = nums[i] + nums[j] +nums[start]+nums[end]
                    
                    if currSum > target :
                        end -=1
                    elif currSum < target :
                        start +=1
                    else:
                        currFourSum =  [nums[i],nums[j],nums[start],nums[end]]
                        if currFourSum not in fourSum:
                            fourSum.append(currFourSum)
                        start +=1
        return fourSum
                        