class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        answer = 0
        while z:
            answer += z&1
            z>>=1
        return answer
        