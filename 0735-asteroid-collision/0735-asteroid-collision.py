class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        """
        [5,10,-5]
        [5] 10 -> 5
        [5,10]
        [-15] -> -15 10
        """
        stack = []
        for i in range(len(asteroids)):
            if stack and  asteroids[i] < 0 and stack[-1] >= 0:
                while stack and abs(asteroids[i]) > stack[-1] and stack[-1] >0 : 
                        stack.pop()
                if not stack or stack[-1] < 0 :
                    stack.append(asteroids[i])
                elif abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                               
            else:
                stack.append(asteroids[i])
        return stack