
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')

        def dfs(node):
            nonlocal max_val

            if not node:
                return 0

            left = max(0, dfs(node.left))
            righ = max(0, dfs(node.right))

            su = left + righ + node.val

            max_val = max(su, max_val)

            return node.val + max(left, righ)

        dfs(root)
        return max_val
