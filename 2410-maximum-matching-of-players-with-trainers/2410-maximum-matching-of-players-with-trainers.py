class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        maximum = 0
        players.sort()
        trainers.sort()
        pointer1 = 0
        pointer2 = 0
        
        while pointer1 < len(players) and pointer2 < len(trainers):
            if players[pointer1] <= trainers[pointer2]:
                maximum += 1
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2 += 1
                
        return maximum