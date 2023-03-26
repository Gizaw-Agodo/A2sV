class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        nums = [(nums[i],i) for i in range(len(nums))]
        
        def merge(left_half, right_half):
            count = 0
            p1 = 0
            p2 = 0
            sorted_arr = []
            while p1 < len(left_half) and p2 < len(right_half):
                if right_half[p2][0] < left_half[p1][0]:
                    count += 1
                    sorted_arr.append(right_half[p2])
                    p2 += 1
                else:
                    sorted_arr.append(left_half[p1])
                    index = left_half[p1][1]
                    answer[index] += count
                    p1 += 1
           
            for i in range(p1,len(left_half)):
                index = left_half[i][1]
                answer[index] += count
                
            sorted_arr.extend(left_half[p1:])
            sorted_arr.extend(right_half[p2:])
            count = 0
            return sorted_arr
        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left)//2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            return merge(left_half, right_half)
        
        ans  = mergeSort(0, len(nums)-1, nums)
        return answer
    
    
