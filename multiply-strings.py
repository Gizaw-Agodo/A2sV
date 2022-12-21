class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = 0
        glob_dec = 1
        for i in reversed(num2):
            dec = 1
            for j in reversed(num1):
                res += int(i) * int(j) * dec * glob_dec
                dec *= 10
            glob_dec*= 10  
        return str(res)
