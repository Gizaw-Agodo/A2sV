class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #handling edje case
        if len(s1) > len(s2):
            return False
        
        # initializing counter dictionaries
        target_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])
        
        for right in range(len(s1),len(s2)):
            if target_count == window_count:
                return True
            
            window_count[s2[right]] += 1
            window_count[s2[right-len(s1)]] -= 1
            if window_count[s2[right-len(s1)]] == 0:
                del window_count[s2[right-len(s1)]]
        
        if window_count == target_count:
            return True
        return False
      
        
        