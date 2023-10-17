class Solution:
    minimum = float("inf")
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = []

        def traverse(node, k):
            if not node or len(smallest) >= k:
                return

            traverse(node.left, k)
            smallest.append(node.val)
            traverse(node.right, k)

        traverse(root, k)
        return smallest[k - 1]
