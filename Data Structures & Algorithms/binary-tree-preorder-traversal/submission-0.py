# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def dfs(node):
            if node is None:
                return

            # add curr node's val to output list first
            out.append(node.val)
            # left path
            dfs(node.left)
            # rigth path
            dfs(node.right)

        res = dfs(root)
        return out

# I think this fits DFS more. So we start from the root, we add it val to the output list, we go to its left subtree recursively and call the same function `dfs`, once we are done we go to the right subtree etc. But for the preorder, we always add first the current node's value then go down the left then the right