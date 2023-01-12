class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = list(words[0])
        for word in words:
            new_temp = []
            for character in word:
                if character in temp:
                    new_temp.append(character)
                    temp.remove(character)
            temp = new_temp
        return temp