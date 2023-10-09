class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1

        m = len(needle) - 1
        initialHash = 0
        
        for index, char in enumerate(needle):
            initialHash += (ord(char) - ord('a') + 1)* 27**(m - index)
        
        windowHash = 0
        for i in range(len(needle)):
            windowHash += (ord(haystack[i]) - ord('a') + 1)* (27**(m - i))
        
        if windowHash == initialHash:
            return 0

        for i in range(len(needle), len(haystack)):
            windowHash -= (ord(haystack[i- len(needle)]) - ord('a') + 1)*(27**m)
            windowHash = (windowHash)*27 + (ord(haystack[i]) - ord('a') + 1)
            if windowHash == initialHash:
                return i - len(needle)  + 1

        return -1
        
       
