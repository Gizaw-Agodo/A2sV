class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        answer = []
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != -1:
                if nums[i] == nums[nums[i]-1]:
                    answer.append(nums[i])
                    break
                else:
                    nums[nums[i]-1], nums[i] = nums[i],nums[nums[i]-1]
                    
        return answer[0]
    