class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        print(path)
        for element in path :
            if element == ".." and len(stack)>0:
                stack.pop()
            elif element not in [".","..",""]:
                stack.append(element)
        answer = "/"+"/".join(stack)
        return answer
    