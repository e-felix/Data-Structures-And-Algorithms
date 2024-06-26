from enum import Enum


class Type(Enum):
    Max = 1
    Min = 2


class Heap:
    def __init__(self, heap_type: Type):
        self.data = []
        self.type = heap_type

    def __compare(self, a, b):
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
        return index * 2 + 1

    def right_child_index(self, index):
        """
        formula = index * 2 + 2
        """
        return index * 2 + 2

    def parent_index(self, index):
        """
        formula = (index - 1) / 2
        """
        assert self.size() > 0

        return int((index - 1) / 2)

    def insert(self, value):
        """
        Insert by default in the end of the array
        Then position it as the correct place ("throttle up")
        """
        self.data.append(value)

        # "Throttle up" to place the value at the correct index
        index = len(self.data) - 1
        while 0 < index < self.size() and self.__compare(self.data[index], self.data[self.parent_index(index)]):
            self.data[index], self.data[self.parent_index(index)] = (
                self.data[self.parent_index(index)],
                self.data[index],
            )

            index = self.parent_index(index)

    def delete(self):
        """
        Remove the root node (as it is the only node which can be deleted)
        by set the last_node as the new root node
        Then move down the new root node to the correct place
        """
        if self.size() <= 1:
            self.data.clear()
            return None

        self.data[0] = self.data.pop()

        # "Trickle node"
        trickle_index = 0

        while self.__has_better_child(trickle_index):
            child_index = self.__get_better_child(trickle_index)

            self.data[trickle_index], self.data[child_index] = (
                self.data[child_index],
                self.data[trickle_index],
            )

            trickle_index = child_index

    def __has_better_child(self, trickle_index):
        """
        Verify if a child should be placed before the node
        i.e for Max HEAP, child is greater
        i.e for Min HEAP, child is lower
        """
        left = False
        right = False

        if self.left_child_index(trickle_index) < self.size():
            left = self.__compare(
                self.data[self.left_child_index(trickle_index)],
                self.data[trickle_index],
            )

        if self.right_child_index(trickle_index) < self.size():
            right = self.__compare(
                self.data[self.right_child_index(trickle_index)],
                self.data[trickle_index],
            )

        return left or right

    def __get_better_child(self, trickle_index):
        if (
                self.right_child_index(trickle_index) < self.size()
                and not self.data[self.right_child_index(trickle_index)]
        ):
            return self.left_child_index(trickle_index)

        if (
                self.right_child_index(trickle_index) < self.size() and
                self.__compare(
                self.data[self.right_child_index(trickle_index)],
                self.data[self.left_child_index(trickle_index)],
        )):
            return self.right_child_index(trickle_index)
        else:
            return self.left_child_index(trickle_index)
