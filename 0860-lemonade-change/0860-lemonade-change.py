class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount = 0
        tenCount = 0
        for bill in bills:
            if bill == 5:
                fiveCount += 1
            elif bill == 10:
                if fiveCount > 0:
                    tenCount += 1
                    fiveCount -= 1
                else:
                    return False
            else:
                if tenCount > 0 and fiveCount > 0:
                    tenCount -= 1
                    fiveCount -= 1
                elif fiveCount >= 3:
                    fiveCount -= 3
                else:
                    return False
        return True