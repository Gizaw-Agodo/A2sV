class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        output = 1
        temp = [1]
        tempString = ""
        i = 0
        j = i+1
        tempString += s[i]
        while i<j and j<len(s):
            if s[i]!=s[j]:
                if s[j] in tempString:
                    i += 1
                    j = i + 1
                    temp.append(output)
                    output = 1
                    tempString = ""
                    tempString += s[i]
                else:
                    tempString += s[j]
                    output += 1
                    j += 1
                    if j==len(s):
                        temp.append(output)
            else:
                i += 1
                j = i + 1
                temp.append(output)
                output = 1
                tempString = ""
                tempString += s[i]
        return max(temp)
