class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = "\n".join(source) + "\n"
        
        i = 0
        response = ''
        while i < len(code):
            if i + 1 < len(code) and code[i] == code[i+1] == '/':
                idx = code.find('\n', i+2)
                i = idx
            elif i + 1 < len(code) and code[i] == '/' and code[i+1] == '*':
                idx = code.find('*/', i+2)
                i = idx + 2
            else:
                response += code[i]
                i += 1
        arr = response.split('\n')
        return filter(len, arr)