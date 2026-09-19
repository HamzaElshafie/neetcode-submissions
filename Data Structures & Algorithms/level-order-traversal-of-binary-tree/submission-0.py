from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return []
            
        queue = deque([root])

        while queue:
            local_res = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                local_res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(local_res)
        
        return res

# queue = [4,5,6,7]

# local_res = [2,3]
# res = [[1]]


# i think that one is a straighforward BFS
# we can have a queue and we always start a fresh new array at each level
# loop through the queue popping them all (since they will be all at same level) and adding them to the list and then at the end we add to the main res list
