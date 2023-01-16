class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        pointer1 = 0
        pointer2 = 0
        maximum = max(len(word1),len(word2))
        i = 0
        while i < maximum:
            if pointer1 < len(word1):
                merged+=word1[pointer1]
                pointer1 +=1
            if pointer2 < len(word2):
                merged+=word2[pointer2]
                pointer2 +=1
            i += 1
        return merged
