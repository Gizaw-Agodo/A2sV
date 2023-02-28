class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        answer = self.isPowerOfFour(n/4)
        return answer