class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(index, count, transfers):
            if index == len(requests):
                if all(t == 0 for t in transfers):
                    return count
                else:
                    return 0
            transfers[requests[index][0]] -= 1
            transfers[requests[index][1]] += 1

            included = backtrack(index + 1, count + 1, transfers)
            transfers[requests[index][0]] += 1
            transfers[requests[index][1]] -= 1

            excluded = backtrack(index + 1, count, transfers)
            return max(included, excluded)

        return backtrack(0, 0, [0]*n )            