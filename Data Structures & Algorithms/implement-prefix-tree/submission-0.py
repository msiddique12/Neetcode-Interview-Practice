class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_end = False     # marks end of word

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #cat
        node = self.root
        for i, c in enumerate(word):
            if c in node.children:
                node = node.children[c]
            else:
                newNode = TrieNode()
                node.children[c] = newNode
                node = node.children[c]

            if i == len(word) - 1:
                node.is_end = True
                
    def search(self, word: str) -> bool:
        node = self.root
        for i, c in enumerate(word):
            if c in node.children:
                node = node.children[c]
            else:
                return False

        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i, c in enumerate(prefix):
            if c in node.children:
                node = node.children[c]
            else:
                return False

        return True
        