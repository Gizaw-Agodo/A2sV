class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp= sorted(nums)
        dic = defaultdict(int)
       
        for i in range(1,len(nums)) :
            if temp[i-1] == temp[i]:
                continue
            else:
                dic[temp[i]] += i
       
        for i in range(len(nums)):
            nums[i] = dic[nums[i]]
        
        return nums
