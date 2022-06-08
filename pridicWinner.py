class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        

        nums_len = len(nums)
        memo = dict()

        def get_scores(left, right):
            if (left, right) in memo: 
                return memo[(left, right)]
            if left==right:
                memo[(left, right)] = nums[left]
                return memo[(left, right)] 
            elif left<right: 
                memo[(left, right)] = max(nums[left] - get_scores(left+1,right),   nums[right] - get_scores(left,right-1))
                return memo[(left, right)]

        diff = get_scores(0, nums_len-1)
        return True if diff>=0 else False
