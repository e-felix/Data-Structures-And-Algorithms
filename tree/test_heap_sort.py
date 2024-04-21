import unittest
from enum import Enum
from heap import Heap, Type


class Ordering(Enum):
    Ascending = 1
    Descending = 2


def heap_sort(data: list, order: Ordering = Ordering.Ascending):
    """
    Use HEAP to sort a list
    """
    type = Type.Min

    if order == Ordering.Descending:
        type = Type.Max

    heap = Heap(type)

    for d in data:
        heap.insert(d)

    new_data = []

    while heap.size() > 0:
        new_data.append(heap.root_node())
        heap.delete()

    return new_data


class TestHeapSort(unittest.TestCase):
    def test_sort_ascending(self):
        data = heap_sort([3, 92, 1, 389, 73])

        self.assertEqual(data, [1, 3, 73, 92, 389])

    def test_sort_descending(self):
        data = heap_sort([3, 92, 1, 389, 73], Ordering.Descending)

        self.assertEqual(data, [389, 92, 73, 3, 1])


if __name__ == "__main__":
    unittest.main()
