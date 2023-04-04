class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def findPrimes(n,left):
            is_prime: list[bool] = [True for _ in range(n)]
            is_prime[0] = is_prime[1] = False
            i = 2

            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j < n:
                        is_prime[j] = False
                        j += i
                i += 1
            ans = []
            for i in range(len(is_prime)):
                if is_prime[i] == True and i >= left:
                    ans.append(i)
            return ans
        
        primes = findPrimes(right + 1,left)
        answer = [-1,-1]
        comparator = float("inf")
        for i in range(len(primes)-1):
            dif =  primes[i+1] - primes[i]
            if dif < comparator:
                answer = [primes[i],primes[i+1]]
                comparator = dif
       
        return answer
        
            