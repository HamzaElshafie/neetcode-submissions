# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)
        
        local = abs(self.get_depth(root.left) - self.get_depth(root.right)) <= 1
        
        return is_left_balanced and is_right_balanced and local
        
    def get_depth(self, node):
        if node is None:
            return 0

        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)
        return 1 + max(left_depth, right_depth)