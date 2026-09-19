# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.get_depth(root)
        
        return self.max_diameter
        
    def get_depth(self, node):
        if node is None:
            return 0
        
        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)

        diameter = left_depth + right_depth
        self.max_diameter = max(self.max_diameter, diameter)
        
        return 1 + max(left_depth, right_depth)