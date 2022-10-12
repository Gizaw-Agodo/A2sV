class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        i = 0
        sumChalk = sum(chalk)
        k%=sumChalk
        print(k)
        while i < n:
            if k < chalk[i]:
                return i
            k-=chalk[i]
            i+=1
