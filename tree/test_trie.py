import unittest
from trie import Trie


class TestTRIE(unittest.TestCase):
    def test_create_trie_and_insert(self):
        """
        Trie
        """
        trie = Trie()
        trie.insert("bat")

        self.assertIsInstance(trie, Trie)
        children = trie.root.children
        self.assertTrue(children.keys().__contains__("b"))

        children = children["b"].children
        self.assertTrue(children.keys().__contains__("a"))

        children = children["a"].children
        self.assertTrue(children.keys().__contains__("t"))


if __name__ == "__main__":
    unittest.main()
