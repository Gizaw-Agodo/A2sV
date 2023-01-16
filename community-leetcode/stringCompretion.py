class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.append("-")
        n = len(chars)
        slow = 0
        fast = 0
        count = 1
        
        for fast in range(n):
            if fast == 0 :
                continue
           
            if chars[fast] == chars[fast-1] :
                count+=1
            else:
                if count == 1:
                    chars[slow] = chars[fast-1]
                    slow+=1
                else:
                    chars[slow] = chars[fast-1]
                    slow+=1
                    if count<10:
                        chars[slow] = str(count)
                        slow+=1
                    else:
                        charnums = list(str(count))
                        for k in charnums:
                            chars[slow] = k
                            slow+=1
                count = 1
            
        for i in range(n-slow):
            chars.pop()
                
                
        return len(chars)
