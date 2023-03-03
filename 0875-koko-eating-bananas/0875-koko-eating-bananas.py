class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findHours(piles, mid ):
            hours = 0
            for pile in piles : 
                if pile <= mid :
                    hours += 1
                else:
                    if pile % mid > 0 : 
                        hours += pile//mid + 1 
                    else:
                        hours += pile//mid   
            return hours
      
        start = 1
        end = max(piles)
        while start <= end : 
            mid = start + (end - start)//2
            hours = findHours(piles, mid)
            if hours > h:
                start = mid + 1
            else:
                end = mid - 1
        return start
                