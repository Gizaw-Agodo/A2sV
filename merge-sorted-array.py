class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        total_len = m+n
        pt1 = m-1
        pt2 = n-1
        pt3 = total_len-1
       
        while pt2 >= 0 :
            if pt1 > 0 and  nums1[pt1] >= nums2[pt2]:
                nums1[pt3] = nums1[pt1]
                pt1 -=1
            else:
                nums1[pt3] = nums2[pt2]
                pt2-=1
            pt3-=1
