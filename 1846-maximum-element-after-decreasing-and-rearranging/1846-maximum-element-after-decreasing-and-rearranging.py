class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(len(arr) - 1):
            curr = arr[i]
            next = arr[i+1]
            if next > curr:
                arr[i+1] = curr + 1
        return arr[-1]
                
        