class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        start = 0
        end = len(skill) -1
        skill.sort()
        chemistry  = 0
        comparator = skill[start] + skill[end]
        while start < end :
            curr_sum = skill[start] + skill[end]
            if curr_sum != comparator :
                return -1
            else:
                chemistry += skill[start]*skill[end]
            start +=1
            end-=1
        return chemistry