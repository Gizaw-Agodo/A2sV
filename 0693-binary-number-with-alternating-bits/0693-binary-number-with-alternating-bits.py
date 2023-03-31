class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n :
            curr_bit = n&1
            n>>=1
            next_bit = n&1
            if curr_bit == next_bit:
                return False
        return True
            