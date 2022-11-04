class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxlen = 0
        start = 0
        curcost = 0
        for i in range(len(s)):
            curcost += abs(ord(s[i])-ord(t[i]))
            while curcost > maxCost:
                curcost -= abs(ord(s[start])-ord(t[start]))
                start +=1
            maxlen = max(maxlen,i-start+1)
        return maxlen
            