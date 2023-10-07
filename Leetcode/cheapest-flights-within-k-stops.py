class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0

        for i in range(k + 1):
            temp_prices = prices.copy()
            for src, dest, cost in flights:
                if prices[src] == float('inf'):
                    continue

                if prices[src] + cost < temp_prices[dest]:
                    temp_prices[dest] = prices[src] + cost

            prices = temp_prices

        return -1 if  prices[dst]  == float('inf') else prices[dst]
