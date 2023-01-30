class Solution:
    def isValid(self, s: str) -> bool:
        parantheses_stack = []
        
        for pars in s:
            if len(parantheses_stack) > 0 and pars == ')' and parantheses_stack[-1] == '(':
                parantheses_stack.pop()
            elif len(parantheses_stack) > 0 and pars == '}' and parantheses_stack[-1] == '{':
                parantheses_stack.pop()
            elif len(parantheses_stack) > 0 and pars == ']' and parantheses_stack[-1] == '[':
                parantheses_stack.pop()
            else:
                parantheses_stack.append(pars)
        return len(parantheses_stack) == 0 
        