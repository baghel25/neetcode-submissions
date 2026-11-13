# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node,dep):
            if not node:
                return None
            if dep == len(res):
                res.append(node.val)
            # res[dep].append(node.val)
            
        
            dfs(node.right,dep+1)
            dfs(node.left,dep+1)

            # if node.right:
            #     res.pop()
                # res.append(node.val)
        dfs(root,0)
        return res


        