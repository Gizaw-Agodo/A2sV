class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt = 0
        for i,w1 in enumerate(words):
            for w2 in words[i+1:]:
                cnt += set(w1) == set(w2)
        return cnt   
