class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(s[0], 1)]
        
        for i in range(1, len(s)):
            if stack:
                letter, count = stack.pop()
                if s[i] == letter:
                    if count + 1 != k:
                        stack.append((letter, count + 1))
                else:
                    stack.append((letter, count))
                    stack.append((s[i], 1))
            else:
                stack.append((s[i],1))
                
        answer = ''
        for letter, count in stack:
            answer += count*letter

        return answer
