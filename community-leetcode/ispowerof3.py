class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        ans = n/3
        
        if ans==3 or ans ==1:
            return True
        elif(ans <3):
            return False
        elif (ans > 3):
            self.isPowerOfThree(ans)
