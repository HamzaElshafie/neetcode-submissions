# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, min_allowed, max_allowed):
            if not node:
                return True
                
            if not (min_allowed < node.val < max_allowed):
                return False
            
            return (
                valid(node.left, min_allowed, node.val)
                and valid(node.right, node.val, max_allowed) 
            )
            

        return valid(root, float("-inf"), float("inf"))
        

# So what i am thinking of is starting at the root, recursively check each node's left and right subtrees with base cases to check the correct condition that each node's left and right children satisfy the condition returning false if we ever have a mismatch during the process