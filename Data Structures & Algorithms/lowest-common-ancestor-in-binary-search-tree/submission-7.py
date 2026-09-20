# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left

            elif p.val > current.val and q.val > current.val:
                current = current.right

            else:
                return current

# If we are at a node that is `p/q` and the other node is reachable from that node, like its below it essentially, then the LCA has to be the node itself right! 

# what if `p` and `q` deviate, so one goes to the left subtree and one goes to the right subtree, then their original parent is the LCA

# so maybe we start from the root, ask are you `p` or `q`? if no we explore the left and right subtrees, if they return p and q to it then this node is the LCA.

# wait acc we can already decide if we explore left and right or just either of them based on the values of the nodes p and q from the beginning