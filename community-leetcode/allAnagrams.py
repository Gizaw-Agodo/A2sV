class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        dic = defaultdict(int)
        answer = []
        for letter in p:
            dic[letter] +=1
        
        start,end = 0 ,0
        counter = len(p)
        
        while end < n :
            if s[end] in dic :
                if dic[s[end]] > 0:
                    counter -=1
                dic[s[end]] -=1
              
            if end-start + 1 == len(p) :
                if counter == 0:
                    answer.append(start)
                
                if s[start] in dic:
                    if dic[s[start]] >=0:
                        counter +=1
                    dic[s[start]] += 1
                start += 1
            end +=1
        return answer
