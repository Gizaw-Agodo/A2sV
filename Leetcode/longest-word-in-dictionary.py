class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
        self.value = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
        curr.value = word
    
    def search(self):
        curr = self.root
        answer = ''
        queue = [curr]
        while queue:
            curr = queue.pop(0)
            for i in range(25, -1, -1):
                letter = curr.children[i]
                if letter != None and letter.is_end:
                    if len(letter.value) >= len(answer): 
                        answer = letter.value
                    queue.append(letter)
        return answer
    



class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.search()
        
