class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        final = ""
        init_index = 0
        
        # looping through each space and splicing the string at that space
        for index in spaces:
            final += s[init_index:index]
            final += " "
            init_index = index
        
        # handling missing strig from the loop 
        final += s[init_index:]
        return final