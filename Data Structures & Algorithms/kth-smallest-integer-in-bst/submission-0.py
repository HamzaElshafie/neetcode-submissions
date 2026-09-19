# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0
        
        def dfs(node):
            nonlocal count, res

            if not node:
                return 
            
            dfs(node.left)

            # increment count
            count += 1

            # condition check for kth smallest val
            if count == k:
                res = node.val
                return

            dfs(node.right) 
        
        dfs(root)
        return res
            
        

# So first of all before thinking of how I will solve it i feel like the solution will have to do with going all the way down the left subtree in DFS fashion and then recursing back incrementing a counter variable k times until we get to the val !? hmmm

# so for a 

#    parent
#    /  \
# left  right

# when left returns to its parent it increments k += 1 
# parent then increments k += 1 because its a valid option
# calls, the right subtree, right subtree increments k += 1

# so like an inorder process

