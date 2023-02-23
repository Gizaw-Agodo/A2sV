class Solution:
    def bestClosingTime(self, customers: str) -> int:
        char_intiger = []
        for char in customers:
            if char == "Y":
                char_intiger.append(1)
            else:
                char_intiger.append(0)
        ones_pref = []
        zero_pref = []
        curr_sum = 0
        for item in char_intiger:
            curr_sum += item
            ones_pref.append(curr_sum)
            
        curr_sum = 0
        for item in char_intiger:
            if item == 0:
                curr_sum += 1
            zero_pref.append(curr_sum)
        
        penality = []
        penality.append(ones_pref[-1])
        for i in range(1,len(customers)):
            penality.append(zero_pref[i-1] + ones_pref[-1]-ones_pref[i-1])
        penality.append(zero_pref[-1])
        print(penality)
        
        min_penality  = penality[0]
        min_index = 0
        for i in range(1,len(penality)):
            if penality[i] < min_penality:
                min_penality = penality[i]
                min_index = i
        return min_index
            
                
        