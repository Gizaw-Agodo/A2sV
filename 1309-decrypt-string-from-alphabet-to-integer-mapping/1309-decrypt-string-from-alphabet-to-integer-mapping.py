class Solution:
    def freqAlphabets(self, s: str) -> str:
            
        answer = ""
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                answer += chr(96 + int(s[i:i+2]))
                i +=3
            else:
                answer += chr(96+int(s[i]))
                i+=1
            
        return answer
                
            