class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        vowels = ['a','e','i','o','u']
        for i in range(len(word)):
            if word[i] in vowels:
                ans += (i + 1)*(len(word)-i)
        return ans
