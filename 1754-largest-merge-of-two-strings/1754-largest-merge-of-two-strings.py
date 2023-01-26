class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        pointer_1 = 0
        pointer_2 = 0
        merge = []
        m = len(word1)
        n = len(word2)
        while pointer_1 < m and pointer_2 < n:
            if word1[pointer_1] > word2[pointer_2]:
                merge.append(word1[pointer_1])
                pointer_1 += 1
                
            elif word1[pointer_1] == word2[pointer_2]:
                if word1[pointer_1:] >= word2[pointer_2:] :
                    merge.append(word1[pointer_1])
                    pointer_1 +=1
                else:
                    merge.append(word2[pointer_2])
                    pointer_2 += 1
            else:
                merge.append(word2[pointer_2])
                pointer_2 += 1
        merge.extend(word1[pointer_1:])
        merge.extend(word2[pointer_2:])
        return "".join(merge)
        
                
                
        