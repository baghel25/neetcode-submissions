# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(node,dep,maxv):
            if not node :
                return None

            # if len(res) == 0:
            #    res.append(node.val)
            #    return

            # if res[dep] > node.val:
            if node.val >= maxv:
              res.append(node.val)
            #   maxv = max_val
            maxv = max(maxv,node.val)

            dfs(node.right,dep+1,maxv)
            dfs(node.left,dep+1,maxv)
            # return 
        
        # res.append(root.val)
        dfs(root,0,float('-inf'))
        # print(res)
        return len(res)

        

        