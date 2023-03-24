class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def queckSort(start, end):
            if end == start:
                return None
            pivot = nums[start]
            read = start + 1
            write = start + 1
            while read < end:
                if nums[read] < pivot:
                    nums[read],nums[write] = nums[write],nums[read]
                    write += 1
                read += 1
            nums[start],nums[write-1] = nums[write-1],nums[start]
            if write-1 == len(nums) - k:
                return nums[write-1]
            left_ans = queckSort(start,write-1)
            if left_ans == None:
                right_ans = queckSort(write,end)
                return right_ans
            return left_ans

        answer = queckSort(0,len(nums))
        return answer if answer != None else nums[-k]
    