class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [f"{nums[0]}"]
       
        ans = []
        start  = 0
        
        for i in range (len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                continue
            else:
                if i - start == 0:
                    ans.append(f"{nums[start]}") 
                else:
                    ans.append(f"{nums[start]}->{nums[i]}")
                start = i + 1
        if start == i+1:
            ans.append(f"{nums[start]}")
        else:
            ans.append(f"{nums[start]}->{nums[i+1]}")
        return ans