class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_array = []
        great_array = []
        equal_array = []
        
        for num in nums:
            if num < pivot:
                less_array.append(num)
            elif num > pivot :
                great_array.append(num)
            else:
                equal_array.append(num)
        return less_array+equal_array+great_array
     