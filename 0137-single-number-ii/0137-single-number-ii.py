class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pos_bit_array = [0]*32
        neg_bit_array = [0]*32
        for i in range(len(nums)):
            bits = bin(nums[i])
            j = 0
            if nums[i] < 0 :
                for k in range(len(bits)-1,2, -1):
                    neg_bit_array[31-j] += int(bits[k])
                    j += 1
            else:
                for k in range(len(bits)-1,1, -1):
                    pos_bit_array[31-j] += int(bits[k])
                    j += 1
        
        pos_answer = 0
        neg_answer = 0
        j = 0
        for i in range(len(pos_bit_array)-1 ,-1 ,-1):
            pos_bit_array[i]  %= 3
            neg_bit_array[i]  %= 3
            pos_answer += pos_bit_array[i]*(2**j)
            neg_answer += neg_bit_array[i]*(2**j)
            j += 1
     
        return -1*neg_answer if neg_answer > pos_answer else pos_answer
        
        
      
            
        