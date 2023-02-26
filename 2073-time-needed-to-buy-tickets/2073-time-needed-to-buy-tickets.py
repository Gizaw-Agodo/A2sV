class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        currPosition = k
        time = 0
        while queue[currPosition] > 0:
            poped = queue.popleft()
            if poped != 0:
                poped -= 1
                time += 1
            queue.append(poped)
            
            if currPosition == 0 :
                currPosition = len(queue)-1
            else:
                currPosition -= 1
                
        return time
            
            
            
        