class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        initial_sum = 0
        answer = []
        
        # calculating the initial even numbers sum
        for num in nums :
            if num%2 == 0 :
                initial_sum += num
        

        for val,index in queries:
            init_num = nums[index]
            updated_num = init_num + val
            nums[index] =  updated_num
            
            # drop from the current number from initial sum if it is even
            if init_num%2 == 0:
                initial_sum -= init_num
            
            # add the updated num to initial sum if it is even
            if updated_num %2 == 0 :
                initial_sum += updated_num
            print(initial_sum)
            answer.append(initial_sum)
            
        return answer
             