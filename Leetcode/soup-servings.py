class Solution:

    def soupServings(self, n: int) -> float:
        if n > 5000: 
            return 1

        @cache
        def recursion ( a, b): 
            if a <= 0 and b <= 0: 
                return 0.5 
            if a<= 0 and b > 0: 
                return 1
            if b <= 0: 
                return 0 
            
            case_1 = recursion(a - 100, b)
            case_2 = recursion(a-75, b - 25)
            case_3 = recursion(a-50, b-50)
            case_4 = recursion(a-25, b-75)
            return 0.25*(case_1 +  case_2 +  case_3 + case_4)

        return recursion(n, n)