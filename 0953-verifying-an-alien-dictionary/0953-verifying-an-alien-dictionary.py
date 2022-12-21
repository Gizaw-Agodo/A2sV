class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        print(dic)
        word_list = []
        for word in words:
            temp_list = []
            for char in word:
                temp_list.append(dic[char])
            word_list.append(temp_list)
              
        if len(word_list) == 1:
            return True
        slow,fast = 0,1
        for i in range(1, len(word_list)):
            if word_list[slow] > word_list[fast]:
                return False
            slow+=1
            fast+=1
            
        return True
            