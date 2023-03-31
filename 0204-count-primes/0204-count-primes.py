class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [True for i in range(n)]
        isPrime[0] = isPrime[1] =  False
        for i in range(2,n-1):
            if isPrime[i]:
                start = 2*i
                while start < n:
                    isPrime[start] = False
                    start += i
        
        return isPrime.count(True)
        