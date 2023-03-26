class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(string, j,k):
            if len(string) == 2*n:
                ans.append(string)
                return 
            if j != 0:
                generate(string+"(",j-1,k)
               
            if j<k:
                print("r",string)
                generate(string+")" ,j,k-1)
              
        ans = []
        openP,closeP = n,n
        generate("",openP,closeP)
        return ans