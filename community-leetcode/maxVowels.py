class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        maximum = 0
        if n < 3 :
            return maximum
        
        vowels = ["a","e","i","o","u"]
        slow,fast = 0,0
        count = 0
        
        while fast < n :
            if s[fast] in vowels:
                count +=1
            
            if fast-slow +1 == k :
                maximum = max(maximum,count)
                
                if s[slow] in vowels:
                    count-=1
                slow+=1
            fast +=1
            
        return maximum
