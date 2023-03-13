class Solution:
    minUnfairness = float('inf')
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(index, distribution):
            if index >= len(cookies):
                maxUnfairness = max(distribution)
                self.minUnfairness = min(self.minUnfairness, maxUnfairness)
                return
            for i in range(k):
                distribution[i] += cookies[index]
                if distribution[i] >= self.minUnfairness:
                    distribution[i] -= cookies[index]
                    continue
                backtrack(index + 1, distribution)
                distribution[i] -= cookies[index]
        backtrack(0, [0]*k)
        return self.minUnfairness