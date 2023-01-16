class Solution(object):
    def decodeString(self, s):
        sta = []
        string = ""
        indSta = []
        num = ""
        prevIsDigit = False
        for i in range(len(s)):
            setNow = False
            if len(sta) == 0 and s[i].isdigit():
                num += s[i]
                prevIsDigit = True
                setNow = True
            elif s[i] == "[":
                sta.append("[")
                indSta.append(i)
            elif s[i] == "]":
                sta.pop()
                temp = indSta.pop()
                if len(sta) == 0:
                    if num is not "":
                        string += int(num)*str(self.decodeString(s[temp+1:i]))
                    else:
                        string+=self.decodeString(s[temp+1:i])
                    num = ""
            elif len(sta) == 0:
                string+=s[i]
            if not setNow:
                prevIsDigit = False
        return string
                
        """
        :type s: str
        :rtype: str
        """
        
