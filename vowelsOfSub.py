class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        vowelList = ['a','e', 'i','o', 'u']
        status = [0]*n
        if word[n-1] in vowelList:
            status[n-1] = 1
            
        for i in range(n-2,-1,-1):
            if word[i] in vowelList :
                    status[i] = n -i +status[i+1]
            else :
                status[i] = status[i+1]
        print(status)
        return sum(status)
