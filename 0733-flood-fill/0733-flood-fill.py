class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [[ False for i in range(len(image[0]))] for _ in range(len(image))]
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def dfs(visited, row, column):
            
            visited[row][column] = True
            temp = image[row][column]
            image[row][column] = color
            
            for i, j in directions:
                new_row = row + i
                new_col = column + j
                if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]):
                    if not visited[new_row][new_col] and image[new_row][new_col] == temp:
                        dfs(visited, new_row, new_col)
        dfs(visited, sr, sc)
        return image
            
        