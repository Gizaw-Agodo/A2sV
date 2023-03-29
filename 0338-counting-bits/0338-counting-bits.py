class Solution:
    def countBits(self, n: int) -> List[int]:
        def findCount(num):
            ans = 1
            while num > 1:
                ans += num&1
                num = num>>1
            return ans
        answer = []
        for i in range(n+1):
            if i == 0 or i == 1:
                answer.append(i)
            else:
                answer.append (findCount(i))
        return answer
            
            
        
        