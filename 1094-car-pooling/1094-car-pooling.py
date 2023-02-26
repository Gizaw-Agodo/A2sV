class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tripList = [0]*1001
        prefSum = 0
        for number, start, end in trips:
            tripList[start] += number
            tripList[end] -= number
            
        for num in tripList:
            prefSum += num
            if prefSum > capacity:
                return False
        return True
            
    