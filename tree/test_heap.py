import unittest
import sys
import io
from heap import Heap, Order


class TestHEAP(unittest.TestCase):
    def test_create_heap(self):
        """
        Heap
        """
        heap = Heap()
        heap.insert(100)

        self.assertIsInstance(heap, Heap)
        self.assertEqual(heap.root_node, 100)

    def test_print_in_order(self):
        """
        HEAP printing In Order
        """
        heap = Heap()
        heap.insert(7)
        heap.insert(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        heap.print(Order.IN_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "7\n10\n12\n")

    def test_print_pre_order(self):
        """
        HEAP printing Pre Order
        """
        heap = Heap()
        heap.insert(7)
        heap.insert(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        heap.print(Order.PRE_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "10\n7\n12\n")

    def test_print_post_order(self):
        """
        HEAP printing Post Order
        """
        heap = Heap()
        heap.insert(7)
        heap.insert(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        heap.print(Order.POST_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "7\n12\n10\n")

    def test_insert(self):
        """
        HEAP insert
        """
        heap = Heap()
        heap.insert(7)
        heap.insert(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        heap.print(Order.IN_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "7\n10\n12\n")

        heap.insert(28)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        heap.print(Order.IN_ORDER)
        self.assertEqual(captureOutput.getvalue(), "7\n10\n12\n28\n")

    def test_delete(self):
        """
        HEAP delete
        """
        heap = Heap()
        heap.insert(7)
        heap.insert(12)
        heap.insert(28)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        heap.print(Order.IN_ORDER)
        self.assertEqual(captureOutput.getvalue(), "7\n10\n12\n28\n")

        heap.delete(12)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        heap.print(Order.IN_ORDER)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureOutput.getvalue(), "7\n10\n28\n")

    def test_search_node(self):
        """
        HEAP search node
        """
        heap = Heap()
        heap.insert(7)
        heap.insert(12)
        heap.insert(11)
        heap.insert(29)
        heap.insert(3)
        heap.insert(1)
        heap.insert(28)
        heap.insert(100)

        value = 29
        searchNode = heap.search(value)

        assert isinstance(searchNode, heap)
        self.assertEqual(value, searchNode.value)

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        searchNode.print(Order.IN_ORDER)
        self.assertEqual(captureOutput.getvalue(), "28\n29\n100\n")


if __name__ == '__main__':
    unittest.main()
