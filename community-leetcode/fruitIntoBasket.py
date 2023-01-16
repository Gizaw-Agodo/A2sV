class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        result=0
        count=defaultdict(int)
        l=0
        for r,t in enumerate(fruits):
            count[t]+=1
            while len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            result=max(result,r-l+1)
        return result
