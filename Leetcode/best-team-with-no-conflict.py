class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        ageScores = [(ages[i],scores[i]) for i in range(len(ages))]
        ageScores.sort(key = lambda x :(x[0],x[1]))
        
        dp = [ageScores[i][1] for i in range(len(ageScores))]

        maxSum = 0
        
        for i in range(len(ageScores)):
            for j in range(i):
                if ageScores[j][1] <= ageScores[i][1]:
                    if dp[j] + ageScores[i][1] > dp[i] :
                        dp[i] = dp[j] + ageScores[i][1]
            maxSum = max(maxSum, dp[i])

        return maxSum


        
