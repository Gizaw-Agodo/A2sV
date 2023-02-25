class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["-","*","/","+"]
        stack = []
        for char in tokens:
            if char in operators :
                num2 = stack.pop()
                num1 = stack.pop()
                val = eval(f'{num1} {char} {num2}')
                if char == "/" :
                    val = ceil(val) if val < 0 else floor(val)
                stack.append(val)
            else:
                stack.append(char)
        return int(stack[0])