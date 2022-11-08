class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        stack = []
        for i in range(len(intervals)):
            if stack and stack[-1][1]>= intervals[i][0]:
                if stack[-1][1] < intervals[i][1]:
                    poped = stack.pop()
                    stack.append([poped[0],intervals[i][1]])
            else:
                stack.append(intervals[i])
        return stack