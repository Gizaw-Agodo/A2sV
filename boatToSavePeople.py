class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(people)
        people.sort()
        
        lower = 0
        higher = n-1
        count = 0
        while lower <= higher:
            if people[lower]+people[higher]<=limit:
                lower+=1
                higher-=1
            else:
                higher -=1
            count+=1
        return count
