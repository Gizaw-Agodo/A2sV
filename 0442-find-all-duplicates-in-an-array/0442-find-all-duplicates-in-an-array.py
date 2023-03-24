class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != -1:
                if nums[i] == nums[nums[i]-1]:
                    answer.append(nums[i])
                    nums[i] = -1
                else:
                    nums[nums[i]-1], nums[i] = nums[i],nums[nums[i]-1]
        return answer
        
                
            
        