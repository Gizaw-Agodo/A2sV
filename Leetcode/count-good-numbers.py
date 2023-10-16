class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        evenPositions = ceil(n/2)
        oddPositions = floor(n/2)
        m = 1000000007

        def findPower(base, power):
            if power == 0:
                return 1
            if power %2 == 0 :
                return findPower((base*base)%m, power//2)%m
            else:
                return (base*findPower((base*base)%m, (power-1)//2))%m
        
        return (findPower(5,evenPositions)*findPower(4,oddPositions)) % (m)
        
