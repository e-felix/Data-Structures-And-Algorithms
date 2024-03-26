import unittest
import sys
import io
from bst import TreeNode, Order


class TestBST(unittest.TestCase):
    def testBST(self):
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

    def testInOrder(self):
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

    def testPreOrder(self):
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

    def testPostOrder(self):
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


if __name__ == '__main__':
    unittest.main()

    # print()
    # print("Deletion")
    # tree.delete(10)
    # print("In Order")
    # tree.print()
    #
    # print()
    # print("Insertion")
    # tree.insert(19)
    # tree.insert(3)
    # tree.insert(1)
    # tree.insert(2)
    # tree.insert(4)
    #
    # print()
    # print("In Order")
    # tree.print()
    #
    # print()
    # print("Search Node")
    # node = tree.search(3)
    # if node is not None:
    #     print("value: ")
    #     print(node.value)
    #     print("tree: ")
    #     node.print()
