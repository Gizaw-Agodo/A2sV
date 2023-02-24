class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for pt in path :
            if pt in ["","."]:
                continue
            elif stack and pt == "..":
                stack.pop()
            elif pt != ".." :
                stack.append(pt)
                
        return "/" + "/".join(stack)