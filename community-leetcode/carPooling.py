class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        length = [0]*1001
        prefSum = 0
        
        for i in range(n):
            length[trips[i][1]] += trips[i][0]
            length[trips[i][2]] -= trips[i][0]
        print(length)
        for trip in length:
            prefSum += trip
            if prefSum > capacity:
                return False
        
        return True
