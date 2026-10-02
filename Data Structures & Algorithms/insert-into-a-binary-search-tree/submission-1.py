# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node, val):
            # base case
            if node is None:
                # create new node & return it
                return TreeNode(val)

            # traverse left subtree
            if val < node.val:
                new_node = insert(node.left, val)
                node.left = new_node
            else:
                new_node = insert(node.right, val)
                node.right = new_node

            return node
            
        return insert(root, val)
        

# So we can start from root, ask if the val is less than or greater than the root. If less then, we go to its left child, if greater we go to the right child. Now this will be recursive. Whats the stopping condition, well if we try to recurse into a child node and its None, this is the place we should create the new node at. 

# I am just wondering whether we would ever need to insert the node mid tree or no? I think no because everyhting is in order so we can never have to