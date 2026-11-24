class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_terminal: bool = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            # place in parent's children
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True


# # prefix = "do"
#         # o
#         *
#     /
#     d
#     |
#     o
#     |
#     g