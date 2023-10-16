class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = self.findPower(x,abs(n))
        if n < 0:
            return 1/answer
        return answer
        
    def findPower(self, x, n):
        # base case
        if n == 0 :
            return 1
        if n % 2 == 0:
            val = self.findPower(x,n//2)
            return val * val
        return x * self.findPower(x, n-1)
        
    
