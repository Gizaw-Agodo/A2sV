class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref_sum = []
        curr_sum = 0
        for i in range(len(self.nums)):
            curr_sum += self.nums[i]
            self.pref_sum.append(curr_sum)
            
       
    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sum[right] - self.pref_sum[left] + self.nums[left]
         


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)