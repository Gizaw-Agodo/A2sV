class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_filtered  = "".join(char for char in start if char != "_")
        target_filtered = "".join(char for char in target if char != "_")
        
        if start_filtered == target_filtered:
            print("gama")
            start_pointer = 0
            target_pointer = 0
            move = 0
            while move < len(start):
                if start[start_pointer] == "L" and target[target_pointer] == "L":
                    if start_pointer < target_pointer:
                        return False
                    else:
                        start_pointer += 1
                        target_pointer += 1
                        move += 1
                elif start[start_pointer] == "R" and target[target_pointer] == "R":
                    if start_pointer > target_pointer:
                        return False
                    else:
                        start_pointer += 1
                        target_pointer += 1
                        move += 1
                elif start[start_pointer] == "_" :
                        start_pointer += 1
                        move += 1
                elif target[target_pointer] == "_" :
                        target_pointer += 1  
            else:
                return True
            
        else:
            return False