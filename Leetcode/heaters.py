class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def binarySearch(house):
            start = 0
            end = len(heaters) - 1
            radius = float('inf')

            while start <= end:
                mid = (end + start)//2
                if heaters[mid] == house:
                    radius = 0
                    break
                elif heaters[mid] > house:
                    radius = min(radius, heaters[mid] - house)
                    end = mid - 1
                else:
                    radius = min(radius, house - heaters[mid])
                    start = mid + 1
            
            return radius
        
        maxRadius = 0
        heaters.sort()    
        for house in houses:
            maxRadius = max(maxRadius, binarySearch(house))
        
        return maxRadius

