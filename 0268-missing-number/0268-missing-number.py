class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def cyclicSort(arr):
            for  i in range(len(arr)):
                while arr[i] != i  and arr[i] != -1:
                    arr[arr[i]],arr[i] = arr[i],arr[arr[i]]
            
            for i in range(len(arr)):
                if arr[i] == -1:
                    return i
        nums.append(-1)
        ans = cyclicSort(nums)
        print(ans)
        return ans