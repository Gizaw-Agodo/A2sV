class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       
        result = n/4
        
        if (result == 4 or result == 1):
            return True
        elif result< 4:
            return False
        elif (n/4 > 4):           
            ispowerOffFour(n)
