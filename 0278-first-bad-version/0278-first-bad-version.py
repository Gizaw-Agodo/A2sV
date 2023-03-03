# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        first_bad = -1
        while start <= end:
            mid = start + (end-start)//2
            is_bad = isBadVersion(mid)
            if is_bad : 
                first_bad = mid
                end = mid - 1
            else:
                start = mid + 1
        return first_bad