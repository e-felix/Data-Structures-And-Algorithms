from enum import Enum


class Order(Enum):
    IN_ORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3


class Heap:
    def __init__(self):
        self.data = []

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

        return self.data[index * 2 + 1]

    def right_child_index(self, index):
        """
        formula = index * 2 + 2
        """
        assert self.size() > 0

        return self.data[index * 2 + 2]

    def parent_index(self, index):
        """
        formula = (index - 1) / 2
        """
        assert self.size() > 0

        return self.data[(index - 1) / 2]

    def print(self, order=Order.IN_ORDER):
        if order == Order.IN_ORDER:
            self.__print_in_order(self)
        elif order == Order.PRE_ORDER:
            self.__print_pre_order(self)
        else:
            self.__print_post_order(self)

    def __print_in_order(self, index=0):
        if index < 0 or index >= self.size():
            return None

        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        self.__print_in_order(left_child_index)
        print(self.data[index])
        self.__print_in_order(right_child_index)

    def __print_pre_order(self, index=0):
        if index < 0 or index >= self.size():
            return None

        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        print(self.data[index])
        self.__print_in_order(left_child_index)
        self.__print_in_order(right_child_index)

    def __print_post_order(self, index=0):
        if index < 0 or index >= self.size():
            return None

        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        self.__print_in_order(left_child_index)
        self.__print_in_order(right_child_index)
        print(self.data[index])
