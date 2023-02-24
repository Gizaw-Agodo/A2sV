class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                next_greater[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            next_greater[nums2[i]] = nums2[i]
            stack.append(i)
            
        for index in stack:
            next_greater[nums2[index]] = -1
      
        ans = []
        for num in nums1:
            ans.append(next_greater[num])
        return ans
    