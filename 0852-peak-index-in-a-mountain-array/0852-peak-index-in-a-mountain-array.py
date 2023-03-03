class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)
        while start <= end : 
            mid = start + (end - start)//2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid-1] < arr[mid] and arr[mid] < arr[mid + 1]:
                start += 1
            elif arr[mid-1] > arr[mid] and arr[mid] > arr[mid + 1]:
                end -= 1

            