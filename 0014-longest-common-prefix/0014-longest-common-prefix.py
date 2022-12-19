class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = min([len(x) for x in strs])
    
        com =''
        for i in range(p):
            co = [x[:p] for x in strs]
            if len(set(co)) == 1:
                return strs[0][:p]
            p-=1
        return ''