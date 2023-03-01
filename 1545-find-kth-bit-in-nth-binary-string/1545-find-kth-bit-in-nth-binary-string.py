class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        n_row = self.findKth(n)
        return n_row[k-1]

    def findKth(self,n):
        if n == 1:
            return "0"
        prev_row = self.findKth(n-1)
        inverted = self.invert(prev_row)
        reverse = self.reverseString(list(inverted))
        n_th_row = prev_row + "1" + reverse
        return n_th_row

   
    def invert(self,previos:string):
        inverted =  ["0" if char == "1" else "1" for char in list(previos)]  
        return "".join(inverted)     
        
    def reverse(self,left,right,s):
        if left >= right:
            return s
        s[left],s[right] = s[right],s[left]
        return self.reverse(left+1,right-1,s)
        
        
    def reverseString(self, s: List[str]) -> None:
        result  = self.reverse(0,len(s)-1,s)
        return "".join(result)
    
        