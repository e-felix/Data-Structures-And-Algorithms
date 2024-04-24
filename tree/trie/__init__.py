class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None

        return currentNode

    def insert(self, word):
        currentNode = self.root

        for char in word:
            if not currentNode.children.get(char):
                currentNode.children[char] = TrieNode()

            currentNode = currentNode.children[char]

        currentNode.children["*"] = None

    def collectAllWords(self, node=None, word="", words=[]):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
                continue

            self.collectAllWords(childNode, word + key, words)

        return words

    def autocomplete(self, prefix):
        node = self.search(prefix)

        if not node:
            return None

        return self.collectAllWords(node, words=[])
