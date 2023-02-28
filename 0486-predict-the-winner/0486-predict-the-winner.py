class Solution:
    def get_score(self, left, right, nums, my_turn):
            #base case
            if left > right :
                return 0
            
            # player1 choose
            if my_turn :
                choose1 = nums[left] + self.get_score(left + 1, right, nums, False)
                choose2 = nums[right] + self.get_score(left, right - 1, nums, False)
                return max(choose1,choose2)
            
            # player2 choose 
            else:
                p2_choose1 = self.get_score(left + 1, right, nums, True)
                p2_choose2 = self.get_score(left, right - 1, nums, True)
                return min(p2_choose1, p2_choose2)
                
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        my_score = self.get_score(0, len(nums)-1, nums, True)
        total = sum(nums)
        p2_score = total - my_score
        return my_score >= p2_score
        
        
            