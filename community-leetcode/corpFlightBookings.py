class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        total = [0]*(n+1)
        
        for i in range(len(bookings)):
            total[bookings[i][0]-1]+= bookings[i][2]
            total[bookings[i][1]]-= bookings[i][2]
        
        for j in range(1,n):
            total[j] +=total[j-1]
        
        return total[:n]
