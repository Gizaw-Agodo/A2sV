class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dic[i+j].append(mat[i][j])
        
        answer = []
        for i in range(len(dic)):
            if i%2 != 0 :
                for j in range(len(dic[i])):
                    answer.append(dic[i][j])
            else:
                for j in range(len(dic[i])-1,-1,-1):
                    answer.append(dic[i][j])
                    
        return answer