class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons  = persons
        self.times = times
        self.winners = [0]*len(persons)
        dic = defaultdict(int)
        maxCount = -1
       
        #finding the winner at each time 
        for i in range(len(persons)):
            dic[persons[i]] += 1
            if dic[persons[i]] >= maxCount:
                maxCount = dic[persons[i]]
                self.winners[i] = persons[i]
            else:
                self.winners[i] = self.winners[i-1]
           

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times)-1
        while left <= right : 
            mid = left + (right-left)//2
            if self.times[mid] > t: 
                right = mid - 1
            elif self.times[mid] <= t:
                left = mid + 1
        return self.winners[left-1]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)


