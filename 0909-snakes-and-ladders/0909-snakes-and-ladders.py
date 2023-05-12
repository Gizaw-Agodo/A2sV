class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        array = [-1]*(n*n)
        
        leftToRight = True
        start = 0
        for i in range(n-1, -1 , -1):
            if leftToRight:
                for j in range(n):
                    array[start] = board[i][j]
                    start += 1
            else:
                for j in range(n-1, -1, -1):
                    array[start] = board[i][j]
                    start += 1
            leftToRight = not leftToRight
       
        
        queue = deque([[1,0]])
        visited = set([1])
        def bfs ():
            
            while queue:
                cell, d = queue.popleft()
                if cell == n*n:
                    return d
                for i in range(1,7):
                    curr = cell + i
                    
                    if curr > n*n:
                        continue
                    if array[curr - 1] != -1:
                        curr = array[curr -1]
                    if  curr not in visited:
                        queue.append([curr , d + 1])
                        visited.add(curr)
            return -1

        return bfs()
                        
                    
                    
                    
            
            