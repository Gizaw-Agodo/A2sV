class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(k, combination, nextt):
            if k == 0:
                answer.append(combination.copy())
            
            for i in range(nextt,n+1):
                combination.append(i)
                backtrack(k-1, combination, i+1)
                combination.pop()
            
        backtrack(k, [], 1)
        return answer
     
                
        