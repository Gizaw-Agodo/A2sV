class DetectSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)]  += 1
        self.points.append(point)
        
    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for x1, y1, in self.points:
            if abs(x-x1) != abs(y-y1) or x==x1 or y == y1 : 
                continue
            ans += self.pointCount[x,y1]*self.pointCount[x1, y]
        return ans
            

        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)