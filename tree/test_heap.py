import unittest
from heap import Heap, Type


class TestHEAP(unittest.TestCase):
    def test_create_heap(self):
        """
        Heap
        """
        heap = Heap(Type.Max)
        heap.insert(100)

        self.assertIsInstance(heap, Heap)
        self.assertEqual(heap.root_node(), 100)
        self.assertEqual(heap.last_node(), 100)

    def test_insert_in_max_heap(self):
        """
        Insert in Max Heap
        """
        heap = Heap(Type.Max)
        heap.insert(7)
        heap.insert(12)
        heap.insert(10)

        self.assertIsInstance(heap, Heap)
        self.assertEqual(heap.root_node(), 12)
        self.assertEqual(heap.last_node(), 10)

    def test_insert_in_min_heap(self):
        """
        Insert in Min Heap
        """
        heap = Heap(Type.Min)
        heap.insert(12)
        heap.insert(10)
        heap.insert(7)

        self.assertIsInstance(heap, Heap)
        self.assertEqual(heap.root_node(), 7)
        self.assertEqual(heap.last_node(), 10)

    def test_delete(self):
        """
        Delete in Max Heap
        """
        heap = Heap(Type.Min)
        heap.insert(12)
        heap.insert(10)
        heap.insert(7)
        heap.insert(14)
        heap.insert(1)
        heap.insert(9)

        self.assertIsInstance(heap, Heap)
        self.assertEqual(heap.root_node(), 1)
        self.assertEqual(heap.last_node(), 10)

        heap.delete()
        self.assertEqual(heap.root_node(), 7)
        self.assertEqual(heap.last_node(), 12)


if __name__ == "__main__":
    unittest.main()
