class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        initial_sum = 0
        answer = []
        for num in nums :
            if num%2 == 0 :
                initial_sum += num
        
        for val,index in queries:
            init_num = nums[index]
            updated_num = init_num + val
            nums[index] =  updated_num
            if init_num%2 == 0:
                initial_sum -= init_num
            if updated_num %2 == 0 :
                initial_sum += updated_num
            print(initial_sum)
            answer.append(initial_sum)
            
        return answer
             