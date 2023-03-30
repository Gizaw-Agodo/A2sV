class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        bit_mask = 0
        while num:
            bit_mask = (bit_mask << 1) | 1
            num >>= 1
        return bit_mask ^ temp 
        
        
        
        
        