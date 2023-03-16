class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        #finding right by binary search
        def findRight(value):
            start = 0
            end = len(intervals) - 1
            while start <= end:
                mid = start + (end - start)//2
                if intervals[mid][0][0] < value:
                    start = mid + 1
                else:
                    end = mid - 1
            return start 
        
       
        answer = [-1]*len(intervals)
         # rearanging and sorting intervals to suit binary search
        intervals = [[intervals[i],i] for i in range(len(intervals))]
        intervals.sort(key = lambda x:x[0][0])
        
        #loop for each valew and find right interval
        for i in range(len(intervals)):
            interval,index = intervals[i]
            temp = findRight(interval[1])
            right_val = intervals[temp][1] if temp < len(intervals) else -1
            if  index != -1 :
                answer[index] = right_val
            
        return answer