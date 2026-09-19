from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # original node -> cloned node
        clones = {
            node: Node(node.val)
        }

        # original nodes still waiting to be inspected 
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    #create the neighbor's clone
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # connect with ??
                clones[curr].neighbors.append(clones[neighbor])

        return clones[node]
        