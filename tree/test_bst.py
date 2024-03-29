import unittest
import sys
import io
from bst import TreeNode, Order


class TestBST(unittest.TestCase):
    def test_create_bst(self):
        """
        BST with 2 children
        """
        tree = TreeNode(10)
        tree.insert(7)
        tree.insert(12)

        self.assertIsInstance(tree, TreeNode)
        self.assertEqual(tree.value, 10)

        left = tree.leftChild
        self.assertIsInstance(left, TreeNode)
        assert isinstance(left, TreeNode)
        self.assertEqual(left.value, 7)

        right = tree.rightChild
        self.assertIsInstance(right, TreeNode)
        assert isinstance(right, TreeNode)
        self.assertEqual(right.value, 12)

    def test_print_in_order(self):
        """
        BST printing In Order
        """
        tree = TreeNode(10)
        tree.insert(7)
        tree.insert(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        tree.print(Order.IN_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "7\n10\n12\n")

    def test_print_pre_order(self):
        """
        BST printing Pre Order
        """
        tree = TreeNode(10)
        tree.insert(7)
        tree.insert(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        tree.print(Order.PRE_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "10\n7\n12\n")

    def test_print_post_order(self):
        """
        BST printing Post Order
        """
        tree = TreeNode(10)
        tree.insert(7)
        tree.insert(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        tree.print(Order.POST_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "7\n12\n10\n")

    def test_insert(self):
        """
        BST insert
        """
        tree = TreeNode(10)
        tree.insert(7)
        tree.insert(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        tree.print(Order.IN_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "7\n10\n12\n")

        tree.insert(28)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        tree.print(Order.IN_ORDER)
        self.assertEqual(captureOutput.getvalue(), "7\n10\n12\n28\n")

    def test_delete(self):
        """
        BST delete
        """
        tree = TreeNode(10)
        tree.insert(7)
        tree.insert(12)
        tree.insert(28)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        tree.print(Order.IN_ORDER)
        self.assertEqual(captureOutput.getvalue(), "7\n10\n12\n28\n")

        tree.delete(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        tree.print(Order.IN_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "7\n10\n28\n")

    def test_search_node(self):
        """
        BST search node
        """
        tree = TreeNode(10)
        tree.insert(7)
        tree.insert(12)
        tree.insert(11)
        tree.insert(29)
        tree.insert(3)
        tree.insert(1)
        tree.insert(28)
        tree.insert(100)

        value = 29
        searchNode = tree.search(value)

        assert isinstance(searchNode, TreeNode)
        self.assertEqual(value, searchNode.value)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        searchNode.print(Order.IN_ORDER)
        self.assertEqual(captureOutput.getvalue(), "28\n29\n100\n")


if __name__ == '__main__':
    unittest.main()
