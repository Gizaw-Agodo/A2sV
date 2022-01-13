class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [-1]
        result = {}
        for i in range(len(nums2)):
            while stack[-1] != -1 and nums2[i] > nums2[stack[-1]]:
                result[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
        output = []
        for i in nums1:
            if i in result:
                output.append(result[i])
            else:
                output.append(-1)
        return output
