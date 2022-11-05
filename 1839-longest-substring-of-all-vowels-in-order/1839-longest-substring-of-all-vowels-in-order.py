class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        maximum = 0
        start = 0
        dic = defaultdict(int)
        for i in range(len(word)):
            dic[word[i]]+=1
            if i == 0 :
                continue
            if ord(word[i])< ord(word[i-1]):
                dic[word[i]]-=1
                if dic[word[i]] == 0:
                    del dic[word[i]]
                if len(dic) == 5:
                    print(dic)
                    maximum = max(maximum,i-start)
                start = i
                dic = defaultdict(int)
                dic[word[i]] = 1
        
        if len(dic)== 5:
            maximum = max(maximum,i-start+1)
        return maximum
                