class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count =  len(set(t))
        dic = defaultdict(int)
        minsize = float("inf")
        target = Counter(t)
        index = None
        left = 0
        count = 0
        
        for right in range(len(s)):
            if s[right] in target:
                dic[s[right]] += 1
                if  dic[s[right]] == target[s[right]]:
                    count += 1
            while count == target_count and left <= right :
                if right-left + 1 < minsize:
                    index = [left,right]
                minsize = min(minsize, right-left + 1 )
                if  s[left] in dic:
                    dic[s[left]] -= 1
                    if dic[s[left]] < target[s[left]]:
                        count -= 1
                left += 1
        return "" if index == None else s[index[0]:index[1]+1]
                
            