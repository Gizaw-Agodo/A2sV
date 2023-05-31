class Solution:
 
    def tribonacci(self, n: int) -> int:
        
        value_0 ,value_1, value_2 = 0,1,1
        
        for i in range(3,n + 1):
            temp_val_2 = value_2
            temp_val_1 = value_1
            
            value_2 = value_0 + value_1 + value_2
            value_1 = temp_val_2
            value_0 = temp_val_1
            
        return value_2 if n != 0 else 0  

        