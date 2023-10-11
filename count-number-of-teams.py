class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        count = 0
        increasing = [0]* len(rating)
        decreasing = [0] * len(rating)

        for i in range(len(rating)-1, -1, -1):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    increasing[i] += 1
                    count += increasing[j]
                else:
                    decreasing[i] += 1
                    count += decreasing[j]
        return count

