class Solution:
    def isPalindrome(self, x: int) -> bool:
        x  = str(x)
        start = 0
        end = len(x)-1
        while start < end :
            if x[start] != x[end]:
                return False
            start +=1
            end-=1
        return True