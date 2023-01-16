    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        output = [0]*len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack !=[] and temp > stack[-1][1]:
                stackInd,stackT = stack.pop()
                output[stackInd] = (i - stackInd)
            stack.append([i,temp])
        return output
