class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findStart():
            exist = False
            start = 0
            end = len(nums)-1
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    exist = True
                    end = mid - 1
                    
            return start if exist else -1
        
        def findEnd():
            exist = False
            start = 0
            end = len(nums)-1
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] > target:
                    end = mid - 1
                elif  nums[mid] < target:
                    start = mid + 1
                else:
                    exist = True
                    start = mid + 1
            return end if exist else -1
        
        return [findStart(),findEnd()]