class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start,end = 0,len(tokens)-1
        maxScore = 0
        score = 0
        
        while start <= end :
            if power >= tokens[start]:
                score +=1
                maxScore = max(maxScore,score)
                power -= tokens[start]
                start +=1
                
            elif score >= 1:
                power += tokens[end]
                score -=1
                end -=1
            
            else:
                return maxScore
        return maxScor
