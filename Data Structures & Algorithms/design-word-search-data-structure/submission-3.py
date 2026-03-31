class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
    
    def dfs(self, node, word, i):
        if i == len(word):
            return node.end

        c = word[i]

        if c != ".":
            if c not in node.children:
                return False
            return self.dfs(node.children[c], word, i+1)
        else:
            for child in node.children.values():
                if self.dfs(child, word, i+1):
                    return True
        return False
