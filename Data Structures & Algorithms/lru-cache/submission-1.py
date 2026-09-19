class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # Create the hashmap
        self.capacity = capacity
        self.cache = {}
        # Create dummy front and tail nodes
        self.front = Node()
        self.tail = Node()
        self.front.next = self.tail
        self.tail.prev = self.front

    def _add_node(self, node: Node):
        current_front_next = self.front.next

        node.prev = self.front
        node.next = current_front_next

        self.front.next = node
        current_front_next.prev = node

    def _remove_node(self, node: Node):
        current_prev = node.prev
        current_next = node.next
        current_prev.next = current_next
        current_next.prev = current_prev
        
    def _move_to_front(self, node: Node):
        # remove node from its pos
        self._remove_node(node)
        # add to front of list
        self._add_node(node)

    def get(self, key: int) -> int:
        # Look up the key in the hashmap and return the value of that
        if key in self.cache:
            node = self.cache[key]
            # Place the node at the front of the list
            self._move_to_front(node)
            return node.value
        # If not found return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # If key is in hashmap move to front
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            node.value = value
        else:
            new_node = Node(key, value)
            # Check we didn't exceed capacity
            if len(self.cache) < self.capacity:
                # Add the key as the key to the hashmap and the value would be the value
                self.cache[key] = new_node 
                # Move to the front of the linkedlist
                self._add_node(new_node)
            else:
                prev_tail = self.tail.prev
                self._remove_node(prev_tail)
                self._add_node(new_node)
                self.cache.pop(prev_tail.key)
                self.cache[new_node.key] = new_node
