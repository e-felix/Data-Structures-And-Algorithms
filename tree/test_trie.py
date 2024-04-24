import unittest
from trie import Trie, TrieNode


class TestTRIE(unittest.TestCase):
    def test_create_trie_and_insert(self):
        trie = Trie()
        trie.insert("bat")

        self.assertIsInstance(trie, Trie)
        children = trie.root.children
        self.assertTrue(children.keys().__contains__("b"))

        children = children["b"].children
        self.assertTrue(children.keys().__contains__("a"))

        children = children["a"].children
        self.assertTrue(children.keys().__contains__("t"))

    def test_search(self):
        trie = Trie()
        trie.insert("bat")
        trie.insert("batman")
        trie.insert("joke")
        trie.insert("joker")

        node = trie.search("ba")

        self.assertIsInstance(node, TrieNode)

    def test_collect_all_words(self):
        trie = Trie()
        trie.insert("bat")
        trie.insert("batman")
        trie.insert("joke")
        trie.insert("joker")

        words = trie.collectAllWords()

        self.assertIsInstance(words, list)
        self.assertListEqual(words, ["bat", "batman", "joke", "joker"])

    def test_autocomplete(self):
        trie = Trie()
        trie.insert("bat")
        trie.insert("batman")
        trie.insert("joke")
        trie.insert("joker")
        trie.insert("jagger")

        suggestions = trie.autocomplete("j")

        self.assertIsInstance(suggestions, list)
        self.assertListEqual(suggestions, ["oke", "oker", "agger"])

        suggestions = trie.autocomplete("jo")

        self.assertListEqual(suggestions, ["ke", "ker"])

        suggestions = trie.autocomplete("joker")

        self.assertListEqual(suggestions, [""])


if __name__ == "__main__":
    unittest.main()
