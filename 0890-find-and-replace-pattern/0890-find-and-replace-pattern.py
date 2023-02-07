class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        ans = []
        for word in words : 
            temp_dic = {}
            temp_string = ""
            for i in range(len(pattern)):
                if pattern[i] in temp_dic:
                    temp_string += temp_dic[pattern[i]]
                else:
                    if word[i] in temp_dic.values():
                        break                        
                    temp_string += word[i]
                    temp_dic[pattern[i]] = word[i]
                    
            if temp_string == word:
                ans.append(word)
        return ans                    
                    
                
        