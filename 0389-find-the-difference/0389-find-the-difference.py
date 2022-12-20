class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if s.count(letter) != t.count(letter):
                return letter