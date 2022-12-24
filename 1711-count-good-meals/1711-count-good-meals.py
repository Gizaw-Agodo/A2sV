class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        answer = 0
        count = defaultdict(int)

        # define all squares of two in range 1- 2^21
        squres_of_two = [2**k for k in range(22)]
        
        for x in deliciousness:
            # compute corsponding element in dic for each x 
            for squre in squres_of_two:
                answer += count[squre-x]
            count[x] +=1
            
        return answer % (10**9 + 7)
        
         