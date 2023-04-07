class Solution:
    def minSteps(self, n: int) -> int:
        
        prime_factors = []
        for i in range(2, n+1):
            while n > 1 and n % i == 0:
                prime_factors.append(i)
                n //= i
        return sum(prime_factors)
        
       
