class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        stack = []
        s.insert(0,"+")
        for i in range(s.length):
            if s[i] =='-':
                stack.append(-int(s[i+1]))
            elif s[i] == "+":
                stack.append(int(s[i+1]))
            elif s[i] == "*":
                stack[-1] = stack.pop()*int(s[i+1])
            elif s[i] == "/":
                stack[-1] = stack.pop()/int(s[i+1])
        
        return sum(stack)
