class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <3:
            return False
        left_max = arr[0]
        left_index = 0
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                left_index = i-1
                break
        right_max = arr[-1]
        right_index = len(arr) - 1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] <= arr[i+1]:
                right_index = i+1
                break
        return left_index == right_index
            
                