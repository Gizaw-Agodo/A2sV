class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        if n == 1:
            return 1
        if n == 0 :
            return  0 
        num1 = self.fib(n-1)
        dp[n-1] = num1
        if n-2 in dp :
            num2 = dp[n-2]
        else:
            num2 =  self.fib(n-2)
        return num1 + num2

        