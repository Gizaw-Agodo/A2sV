class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        def gcd(num1,num2):
            if num2 == 0:
                return num1
            return gcd(num2, num1%num2)
    
        count = Counter(deck)
        value_list = list(count.values())
        temp = 0
        for i in range(len(value_list)):
            maximum  = max(value_list[i],temp)
            minimum = min(value_list[i],temp)
            cur_gcd = gcd(maximum,minimum)
            if cur_gcd == 1:
                return False
            temp = cur_gcd
        return True
            