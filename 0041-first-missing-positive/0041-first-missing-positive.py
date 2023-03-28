class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def cyclicSort(arr):
            for  i in range(len(arr)):
                while arr[i] != i + 1:
                    if arr[i]-1 < len(arr) and arr[i]-1 >= 0:
                        if arr[arr[i]-1] == arr[i]:
                            break
                        arr[arr[i]-1],arr[i] = arr[i],arr[arr[i]-1]
                    
                    else:
                        break
            return arr                    
        temp = cyclicSort(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                count += 1
                if count != nums[i]:
                    return count
        return count + 1     
            
               
           
                
                
                
            
            
        