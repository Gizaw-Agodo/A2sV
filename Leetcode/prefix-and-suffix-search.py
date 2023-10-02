class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, i):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.index = i

    def search(self, word):
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return -1
        return curr.index
    


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for index, word in enumerate(words):
            for i in range(len(word)-1 , -1 , -1):
                self.trie.insert(word[i: ] + '#' + word, index )


    def f(self, pref: str, suff: str) -> int:
        trie = self.trie
        index = trie.search(suff + '#' + pref)
        return index
         
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
