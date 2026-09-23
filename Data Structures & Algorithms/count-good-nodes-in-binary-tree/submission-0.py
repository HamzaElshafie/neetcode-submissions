# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def isGood(node, max_seen):
            nonlocal good_nodes

            if not node:
                return
            if node.val >= max_seen:
                good_nodes += 1
                max_seen = node.val
            
            isGood(node.left, max_seen)
            isGood(node.right, max_seen)

        
        isGood(root, float("-inf"))
        return good_nodes

# I think this one also would work with a DFS. Every node can only have one parent. The root should always be added to the list of good nodes.