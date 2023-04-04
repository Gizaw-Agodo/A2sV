class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maskDic = defaultdict(int)
        for word in words:
            for letter in word:
                maskDic[word]|= 1<< ord(letter) - ord("a")
        maximum = 0
        for i in range(len(words)):
            for j in range(i + 1,len(words)):
                if maskDic[words[i]] & maskDic[words[j]] ==0:
                    maximum = max(maximum,len(words[i])*len(words[j]))
        return maximum
            
            
        