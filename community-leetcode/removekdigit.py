def removeKdigits(num, k):
        if len(num) == 1 and k == 1:
            return "0"
        
        stack = []
        popped = 0
        i = 0
        while i < len(num):
            while (stack and num[i] < stack[-1]) and popped < k:
                stack.pop()
                popped += 1
            stack.append(num[i])
            if popped == k:
                break
            i += 1
            
        if popped < k:
            for j in range(k - popped):
                stack.pop()
                
        stack.extend(num[i+1:])
        
        while stack and stack[0] == "0":
            stack.pop(0)
            
        if len(stack) == 0:
            return "0"
        return "".join(stack)
