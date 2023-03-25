class Solution:
    def maxLength(self, arr: List[str]) -> int:
        answer = 0
        def backtrack(conc, start):
            nonlocal answer
            temp_str = "".join(conc)
            if len(temp_str) > len(set(temp_str)):
                return
            answer = max(answer, len(temp_str))
            for i in range(start, len(arr)):
                conc.append(arr[i])
                backtrack(conc, i + 1)
                conc.pop()
        backtrack([],0)
        return answer