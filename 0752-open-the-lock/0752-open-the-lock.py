class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        
        queue = deque([["0","0","0","0"]])
        visited = set(deadends)
        visited.add('0000')
      
        
        if '0000' in deadends:
            return -1
        
        def bfs(target):
            
            level = 1
            
            while queue:
                
                length = len(queue)
                
                for k in range(length):
                    string = queue.popleft()
                    
                    for i in range(4):
                        for direction in [1, -1] :
                            tempstring = string.copy()
                            tempstring[i] = str((int(string[i]) + direction)% 10) 
                            curstr = "".join(tempstring)
                            
                            if curstr == target:
                                return level
                            if  curstr not in visited:
                                queue.append(tempstring)
                                visited.add(curstr)
                level += 1
            return -1
        
        return 0 if  target == "0000" else bfs(target)
                
           
                
       