class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        square_list = []
        start = 0
        while start*start <= c:
            square_list.append(start)
            start +=1
        
        start = 0
        end = len(square_list)-1
        print (end)
        while start <= end :
            if square_list[start]**2 + square_list[end]**2 == c : 
                return True
            elif square_list[start]**2 + square_list[end]**2 < c : 
                start +=1
            else:
                end -=1
        return False
            
                
            