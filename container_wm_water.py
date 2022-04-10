class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start,end = 0,len(height)-1
        area = 0
        while start < end:
            newarea = (end-start)*min(height[end],height[start])
            area = max(area,newarea)
            if height[start] < height[end]:
                start+=1
            else:end-=1
        return area
