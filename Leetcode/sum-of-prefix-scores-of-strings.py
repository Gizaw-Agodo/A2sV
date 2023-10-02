class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.count = 0
    

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.count += 1
    
    def findScore(self, word):
        curr = self.root
        score = 0
        for char in word: 
            index = ord(char) - ord('a')
            score += curr.children[index].count
            curr = curr.children[index]
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        answer = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            score = trie.findScore(word)
            answer.append(score)
        return answer
        
