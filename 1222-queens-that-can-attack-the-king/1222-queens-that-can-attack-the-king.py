class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        



        queen_set = {(i, j) for i, j in queens}
        res = []
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        
        for dx, dy in direction:
            king_x, king_y = king[0], king[1]
            
            while 0 <= king_x < 8 and 0 <= king_y < 8:
                king_x += dx
                king_y += dy
                
                if (king_x, king_y) in queen_set:
                    res.append([king_x, king_y])
                    break
        return res
    

                