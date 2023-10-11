class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirRep = {"N" :[0, 1], "E":[1, 0], "W":[-1, 0], "S":[0,-1]}
        leftRep = {"N":"W", "W":"S", "S":"E", "E":"N"}
        rightRep = {"N":"E", "E":"S", "S":"W", "W":"N"}
        
        instructions = instructions*4
        currDir = ["N", 0, 0]

        for char in instructions:
            dir, x, y = currDir
            if char == "G":
                x += dirRep[dir][0]
                y += dirRep[dir][1]
            elif char == "R":
                dir = rightRep[dir]
            elif char == "L":
                dir = leftRep[dir]

            currDir = [dir, x, y]

        if currDir == ["N",0,0]:
            return True
        
        return False




