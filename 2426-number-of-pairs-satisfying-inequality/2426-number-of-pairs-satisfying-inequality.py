class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:    
        answer = 0
        def binarySearch(start , end, arr,target):
            while start <= end :
                mid = start + (end-start)//2
                if arr[mid] <= target:
                    start = mid + 1
                elif arr[mid] > target : 
                    end = mid - 1
            return start
        
        
        def merge(left_half , right_half):
            nonlocal answer
            p1 = 0
            p2 = 0
            ans = []
            for i in range(len(right_half)):
                temp = binarySearch(0,len(left_half)-1,left_half,right_half[i] + diff)
                answer += temp
            
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
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half= mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)
        
        transformed = [nums1[i]-nums2[i] for i in range(len(nums1))]
        mergeSort(0, len(transformed)-1, transformed)
        return answer
        
    
            
            