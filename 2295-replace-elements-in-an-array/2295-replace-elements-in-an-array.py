class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for key,value in reversed(operations):
            dic[key] = dic.get(value,value)
        print(dic)
        for index,num in enumerate(nums):
            if num in dic:
                nums[index] = dic[num]
        return nums