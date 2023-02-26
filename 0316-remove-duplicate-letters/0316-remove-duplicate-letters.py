class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        lastOccurance = defaultdict(int)
        for i in range(len(s)):
            lastOccurance[s[i]] = i
            
        for index, char in enumerate(s):
            if char not in stack:
                while stack and char < stack[-1] and lastOccurance[stack[-1]] > index:
                    stack.pop()
                stack.append(char)
            
        return "".join(stack)
                
            
        