class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        solved = {}
        solved[n-1] = questions[n-1][0]

        for i in range(n-2,-1,-1):
            if i + questions[i][-1]+1 <n:
                solved[i] = max(solved[i+1],questions[i][0]+solved[i+questions[i][-1]+1])
            else:
                solved[i] = max(solved[i+1],questions[i][0])
        maximum = 0
        for i in range(len(solved)) :
            if solved[i] > maximum:
                maximum = solved[i]
        return maximum 
