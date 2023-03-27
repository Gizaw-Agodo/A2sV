class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        answer = 0
        def binarySearch(start , end, arr,target):
            while start <= end :
                mid = start + (end-start)//2
                if arr[mid] <= target:
                    start = mid + 1
                elif arr[mid] > target : 
                    end = mid - 1
            return len(arr) - start 
        
        def merge(left_half, right_half):
            nonlocal answer
            
            for i in range(len(right_half)):
                temp = binarySearch(0,len(left_half)-1,left_half,right_half[i]*2)
                answer += temp
                
            count = p1 = p2 = 0
            ans = []
            while p1 < len(left_half) and p2 < len(right_half):
                if left_half[p1] <= right_half[p2]:
                    ans.append(left_half[p1])
                    p1 += 1
                else:
                    ans.append(right_half[p2])
                    p2 += 1
            ans.extend(left_half[p1:])
            ans.extend(right_half[p2:])
            return ans
        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            
            mid = left + (right - left)//2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            return merge(left_half, right_half)
        
        mergeSort(0, len(nums)-1, nums)
        ans = binarySearch(0,4,[1,2,3,4,5],3)
        print(ans)
        return answer