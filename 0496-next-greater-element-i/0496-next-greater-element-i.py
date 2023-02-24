class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = []
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                next_greater[stack[-1]] = nums2[i]
                stack.pop()
            next_greater.append(nums2[i])
            stack.append(i)
            
        for index in stack:
            next_greater[index] = -1
       
        dic = {}
        for i in range(len(nums2)):
            dic[nums2[i]] = next_greater[i]
        ans = []
        for num in nums1:
            ans.append(dic[num])
        return ans
    