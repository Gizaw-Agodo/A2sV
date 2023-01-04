class Solution:
    def printVertically(self, s: str) -> List[str]:
        splited_s = s.split(" ")
        sorted_s = sorted(splited_s, key = len, reverse = True)
        reverse = [[" "]*len(splited_s) for i in range(len(sorted_s[0]))]
        print(reverse)
       
        for i in range(len(splited_s)):
            for j in range(len(splited_s[i])):
                reverse[j][i] = splited_s[i][j]
        
        answer = []
        for element in reverse:
            temp = ""
            for s in element : 
                temp +=s
            answer.append(temp.rstrip())
            
        return answer
    
        
        