class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()

        def binarySearch(num, temp, start, end):

            while start <= end:
                mid = start + (end - start)//2
                if temp[mid] >= num:
                    end = mid - 1
                else:
                    start = mid + 1
            return start
        
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                temp.append(nums[i])

        n = len(nums)
        maximum = float('-inf')
 
        for i in range(len(temp)):
            maxBound = binarySearch(temp[i] + n ,temp, i, len(temp) - 1)
            maximum = max(maximum, maxBound - i)
            
        return n - maximum 

