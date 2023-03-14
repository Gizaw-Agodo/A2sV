class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        stack = []
        def backtrack(index):
            if index >= len(num):
                return len(stack) > 2 and stack[-1] == stack[-2]+stack[-3]
            
            for i in range(index,len(num)):
                value = int(num[index:i+1])
                if len(stack) < 2 or value == stack[-1] + stack[-2]:
                    stack.append(value)
                    if num[index] == "0" and int(value) > 0:
                        stack.pop()
                        continue
                    if backtrack(i + 1):
                        return True
                    stack.pop()
            return False
        return(backtrack(0))