from enum import Enum


class Type(Enum):
    Max = 1
    Min = 2


class Heap:
    def __init__(self, type: Type):
        self.data = []
        self.type = type

    def compare(self, a, b):
        if self.type == Type.Max:
            return a > b

        if self.type == Type.Min:
            return a < b

    def size(self):
        return len(self.data)

    def root_node(self):
        assert self.size() > 0

        return self.data[0]

    def last_node(self):
        assert self.size() > 0

        return self.data[-1]

    def left_child_index(self, index):
        """
        formula = index * 2 + 1
        """
        assert self.size() > 0

        return index * 2 + 1

    def right_child_index(self, index):
        """
        formula = index * 2 + 2
        """
        assert self.size() > 0

        return index * 2 + 2

    def parent_index(self, index):
        """
        formula = (index - 1) / 2
        """
        assert self.size() > 0

        return int((index - 1) / 2)

    def insert(self, value):
        self.data.append(value)

        # "Throttle up" to place the value at the correct index
        index = len(self.data) - 1
        while index > 0 and self.compare(
            self.data[index], self.data[self.parent_index(index)]
        ):
            self.data[index], self.data[self.parent_index(index)] = (
                self.data[self.parent_index(index)],
                self.data[index],
            )

            index = self.parent_index(index)
