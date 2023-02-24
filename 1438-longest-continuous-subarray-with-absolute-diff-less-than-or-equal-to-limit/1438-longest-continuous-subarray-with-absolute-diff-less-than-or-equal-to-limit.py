class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        left = 0
        longest_size = 0
        
        for right in range(len(nums)):
            while decreasing and nums[right] > decreasing[-1]:
                decreasing.pop()
            decreasing.append(nums[right])
            
            while increasing and nums[right] < increasing[-1]:
                increasing.pop()
            increasing.append(nums[right])   
                
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1
            longest_size = max(longest_size,right-left + 1 )
            
        return longest_size