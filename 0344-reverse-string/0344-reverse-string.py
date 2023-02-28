class Solution:
    
    def reverse(self,left,right,s):
        if left >= right:
            return 
        s[left],s[right] = s[right],s[left]
        self.reverse(left+1,right-1,s)
        
    def reverseString(self, s: List[str]) -> None:
        self.reverse(0,len(s)-1,s)
     