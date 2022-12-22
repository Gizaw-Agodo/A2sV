class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        lossers = defaultdict(int)
        players = set()
        
        all_winners = []
        one_losers = []
       
        for i in range(len(matches)):
            winners[matches[i][0]] +=1
            lossers[matches[i][1]] +=1
            players.add(matches[i][0])
            players.add(matches[i][1])

           
        for player in players:
            if winners[player] == winners[player] + lossers[player]:
                all_winners.append(player)
            elif winners[player] == winners[player]+lossers[player]-1:
                one_losers.append(player)     
        all_winners.sort()
        one_losers.sort()
        return [all_winners,one_losers]