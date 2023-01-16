class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        matrix = [[False for i in range(n)]for j in range(n)]
        
        start = 0
        pal_len = 1
        
        for i in range(n):
            matrix[i][i] = True
            
         #  for strings with length 2
        for i in range(n-1):
            if s[i]== s[i+1]:
                matrix[i][i+1] = True
                start = i
                pal_len = 2
                
         #   for strings of lengthe >=3
        
        for l in range(3,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j] and matrix[i+1][j-1] == True:
                    matrix[i][j] = True
                
                    if l > pal_len :
                        start = i 
                        pal_len = l
                        
        return s[start:start+pal_len]
        