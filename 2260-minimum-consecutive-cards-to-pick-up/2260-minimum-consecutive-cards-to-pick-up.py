class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic =  defaultdict(int)
        minimum = float(inf)
        start = 0
        for i in range(len(cards)):
            dic[cards[i]] +=1
            if dic[cards[i]] > 1 :
               
                while cards[i] != cards[start]:
                    dic[cards[start]] -=1
                    start +=1
              
                minimum = min(minimum,i-start+1)
                dic[cards[start]]-=1
                start +=1
        return minimum if minimum != float(inf) else -1