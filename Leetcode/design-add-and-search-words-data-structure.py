class WordDictionary:

    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
        
    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = WordDictionary()
            curr = curr.children[index]
        
        curr.isEndOfWord = True;
        

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i+1:]): return True
                return False
            index = ord(c) - ord('a')
            
            if curr.children[index] == None:
                 return False
            curr = curr.children[index]
        
        return curr != None and curr.isEndOfWord
