class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        
        current_row = [poured]  
        answer = current_row
        
        for i in range(query_row + 1):
            
            next_row = [0]*(len(current_row) + 1)
            
            for j in range(len(current_row)):
                
                if current_row[j] >= 1:
                    given = (current_row[j] - 1)/2
                    next_row[j] += given
                    next_row[j+1] += given
                    current_row[j] = 1
                    
            answer = current_row
            current_row = next_row
        return answer[query_glass]

                
                
                
            