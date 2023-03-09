class Solution:
    def splitString(self, s: str) -> bool:
        stack = []
        def backtrack(index):
            if index >= len(s):
                return len(stack) >= 2
            for i in range(index,len(s)):
                value = int(s[index:i+1])
                if not stack or value + 1 == stack[-1]:
                    stack.append(value)
                    if backtrack(i + 1):
                        return True
                    stack.pop()
            return False
        return(backtrack(0))
        
        
        
   
                
                
        