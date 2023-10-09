

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def getPath(path,element,node):

            if node == None:
                return (False,path)

            path.append(node)
           
            if node == element:
                return (True, path)

            isInLeft,path1 = getPath(path, element, node.left)
            isInRight,path2 = getPath(path, element, node.right)

            if isInLeft :
                return (True, path1)
                
            elif isInRight:
                return (True, path2)

            path.pop()
            return (False,path)
        
        truth1, path_1 = getPath([], p, root)
        truth2, path_2 = getPath([], q, root)

        i = 0
        while i < len(path_1) and i < len(path_2):
            if path_1[i] != path_2[i]:
                break
            i += 1
       
        return path_1[i-1]
