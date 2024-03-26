from enum import Enum


class Order(Enum):
    IN_ORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3


class TreeNode:
    """Binary Search Tree (BST) implementation"""

    def __init__(
        self,
        value,
        leftChild=None,
        rightChild=None
    ):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

    def insert(self, value):
        """
        1: if value is less than node value, insert into the left child
        2: if value is greater than node value, insert into the right child
        3: Recursively repeat step 1 and 2
           until reaching the end to insert the value
        """
        if value < self.value:
            if self.leftChild is None:
                self.leftChild = TreeNode(value)
            else:
                self.leftChild.insert(value)
            return

        if value > self.value:
            if self.rightChild is None:
                self.rightChild = TreeNode(value)
            else:
                self.rightChild.insert(value)

    def delete(self, value):
        return self.__delete(value, self)

    def __delete(
        self, value,
        node=None
    ):
        """
        Base case - we reached the bottom of the tree
        and the parent does not have children
        """
        if node is None:
            return None

        # If the value to delete is less or greater than the current node value
        # we set the left or the right child
        # to be the return node of this recursive method
        if value < node.value:
            node.leftChild = node.__delete(value, node.leftChild)

            # We return the current node & its subtree to be used as the new value
            # of the parent node (left or right)
            return node

        if value > node.value:
            node.rightChild = node.__delete(value, node.rightChild)
            return node

        if value == node.value:
            if node.leftChild is None:
                # If the current node does not have a leftChild
                # we delete it by returning its rightChild
                # to be its parent's new subtree
                return node.rightChild

            if node.rightChild is None:
                return node.leftChild

            # If the current node has no children, we delete the current node
            # by calling the lift method to chnage the current node value
            # by the value of the successor node
            node.rightChild = self.__lift(node.rightChild, node)
            return node

    def __lift(self, node, nodeToDelete):
        """
        If node has a leftChild, recursively call this method
        to continue down the left subtree to find the
        successor node.
        """
        if node.leftChild:
            node.leftChild = self.__lift(node.leftChild, nodeToDelete)
            return node

        # If node has no left child, it means the node is the
        # successor node, and we take its value
        # and make it the new value of the node we are deleting
        nodeToDelete.value = node.value

        # We return the successor node's rightChild to be used
        # as the parent left child
        return node.rightChild

    def print(self, order=Order.IN_ORDER):
        if order == Order.IN_ORDER:
            self.__print_in_order(self)
        elif order == Order.PRE_ORDER:
            self.__print_pre_order(self)
        else:
            self.__print_post_order(self)

    def __print_in_order(self, node=None):
        if node is None:
            return

        self.__print_in_order(node.leftChild)
        print(node.value)
        self.__print_in_order(node.rightChild)

    def __print_pre_order(self, node=None):
        if node is None:
            return

        print(node.value)
        self.__print_pre_order(node.leftChild)
        self.__print_pre_order(node.rightChild)

    def __print_post_order(self, node=None):
        if node is None:
            return

        self.__print_post_order(node.leftChild)
        self.__print_post_order(node.rightChild)
        print(node.value)

    def search(self, value):
        return self.__search(value, self)

    def __search(self, value, node):
        if node is None or node.value == value:
            return node

        if value > node.value:
            if node.rightChild is None:
                return None

            return self.__search(value, node.rightChild)

        if value < node.value:
            if node.leftChild is None:
                return None

            return self.__search(value, node.leftChild)
