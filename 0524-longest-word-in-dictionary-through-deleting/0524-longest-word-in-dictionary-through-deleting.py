class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x :(-len(x),x))
        
        for i in range(len(dictionary)):
            j = 0
            for letter in s:
                if j < len(dictionary[i]) and letter == dictionary[i][j]:
                    j+=1
                if j == len(dictionary[i]):
                    return dictionary[i]
        return ""