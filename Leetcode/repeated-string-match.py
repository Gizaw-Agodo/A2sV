class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        # kmp -> string search algorithm 
        
        count = 1
        tempA = a
        while len(tempA) < len(b):
            tempA += a
            count += 1
        
        def checkSubstring(string, subString):

            n = len(subString)
            lsp = [0]*n
            slow = 0
            fast = 1
            while fast < n:
                if subString[fast] == subString[slow]:
                    lsp[fast] = slow + 1
                    fast += 1
                    slow += 1
                else:
                    if slow == 0:
                        fast += 1
                    else:
                        slow = lsp[slow - 1]

            p1 = 0 
            p2 = 0

            while p2 < len(string):
                if subString[p1] == string[p2]:
                    p1 += 1
                    p2 += 1
                
                elif p1 == 0:
                    p2 += 1
                    
                else:
                    p1 = lsp[p1 - 1]

                if p1 == len(subString):
                    return True
                
            return False
       
        if checkSubstring(tempA, b) :  return count
        if checkSubstring(tempA + a , b) : return count + 1
        return -1
