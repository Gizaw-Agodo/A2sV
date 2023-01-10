class Solution:
    def sumOfThree(self, num: int) -> List[int]:
         # derived using math formula x +x+1 +x +2 = num
        if (num -3)%3 !=0:
            return []
        x = (num-3)//3
        return [x,x+1,x+2]
