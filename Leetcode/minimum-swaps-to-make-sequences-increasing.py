class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp (index, preva, prevb):
            
            if index == len(nums1):
                return 0
            
            swap = float('inf') 
            notswap = float('inf')

            if nums1[index] >  preva and nums2[index] > prevb:
                notswap = dp(index + 1, nums1[index],nums2[index])
            if nums2[index] > preva and nums1[index] > prevb:
                swap = 1 + dp(index + 1, nums2[index],nums1[index])
           
            return min(swap, notswap)

        return dp(0, -1,-1)

