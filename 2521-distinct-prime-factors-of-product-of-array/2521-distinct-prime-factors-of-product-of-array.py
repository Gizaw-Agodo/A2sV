class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def findUniquePrimeFactors(n):
            factorization = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factorization.add(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.add(n)
            return factorization
        
        uniquePrimes = set()
        for i in range(len(nums)):
            currPrimes = findUniquePrimeFactors(nums[i])
            uniquePrimes = uniquePrimes.union(currPrimes)
     
        return len(uniquePrimes)
