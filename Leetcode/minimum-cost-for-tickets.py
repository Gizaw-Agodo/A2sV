class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @cache
        def recursion(day):
            if day > days[-1]:
                return 0
            
            if day in day_set:
                value1 = costs[0] + recursion(day + 1)
                value2 = costs[1] + recursion(day + 7)
                value3 = costs[2] + recursion(day + 30)
                return min(value1, value2, value3)
            
            return recursion(day + 1)
            
        day_set = set(days)            
        return recursion(days[0])
        
            

