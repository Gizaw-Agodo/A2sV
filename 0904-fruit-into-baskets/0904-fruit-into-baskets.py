class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        countDic = defaultdict(int)
        maxCount = 0
        left = 0
        for right in range(len(fruits)):
            countDic[fruits[right]] += 1 
            while len(countDic) > 2:
                countDic[fruits[left]] -= 1
                if countDic[fruits[left]] == 0:
                    del countDic[fruits[left]]
                left += 1
            maxCount = max(maxCount , right - left + 1)
       
        return maxCount
            
        