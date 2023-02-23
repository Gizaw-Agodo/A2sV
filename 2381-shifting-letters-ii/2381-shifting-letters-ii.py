class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref_sum  = [0]*(len(s)+1)
        
        for start,end,shift in shifts:
            if shift == 0:
                pref_sum[start] -= 1
                pref_sum[end+1] += 1
            else:
                pref_sum[start] += 1
                pref_sum[end+1] -= 1
        
        ans = list(s)
        for i in range(len(s)):
            if i != 0 :
                pref_sum[i] += pref_sum[i-1]
            if pref_sum[i] < 0 :
                order = ord(ans[i]) - (abs(pref_sum[i])%26) 
                if order < 97 :
                    order += 26
                ans[i] = chr(order)
            else:
                order = ord(ans[i]) + pref_sum[i]%26
                if order > 122:
                    order -= 26
                ans[i] = chr(order)
        return "".join(ans)
                
            
        