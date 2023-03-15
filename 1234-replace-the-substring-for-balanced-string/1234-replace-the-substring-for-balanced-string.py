class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        appear = len(s)//4
        overflow = defaultdict(int)
        for key in count :
            diff =  count[key] - appear
            if diff > 0:
                overflow[key] = diff
        
        start = 0
        answer = float("inf")
        replaced = sum(overflow.values())
        if replaced == 0:
            return 0
        for i in range(len(s)):
            if s[i] in overflow:
                if overflow[s[i]] > 0:
                    replaced -= 1
                overflow[s[i]] -= 1
                
            while replaced == 0 and start <= i:
                answer = min(answer, i - start + 1 )
                if s[start] in overflow:
                    if overflow[s[start]] == 0:
                        replaced += 1
                    overflow[s[start]] += 1
                start += 1                
        return 0 if answer == float("inf") else answer
                
            
                
        