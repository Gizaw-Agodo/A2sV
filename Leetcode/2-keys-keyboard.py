class Solution:
    def minSteps(self, n: int) -> int:
        # # mathematical approach
        # prime_factors = []
        # for i in range(2, n+1):
        #     while n > 1 and n % i == 0:
        #         prime_factors.append(i)
        #         n //= i
        # return sum(prime_factors)

        # dp approach
        memo = {}
        def dp(curr_len,copy_len):
            if curr_len == n:
                return 0
            
            if curr_len > n : 
                return float('inf')
            index = (curr_len , copy_len)
            if index in memo:
                return memo[index]

            temp_len = curr_len + copy_len

            copy_paste = 2 + dp(curr_len + curr_len, curr_len)

            paste = float('inf')
            if copy_len:
                paste = 1 + dp(temp_len , copy_len)
            
            memo[index] = min(copy_paste,paste)
            return memo[index]
        
        return dp(1,0)
        
       
