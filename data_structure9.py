from __future__ import annotations

from typing import Any


class BinaryTree:
    def __init__(self, value: Any) -> None:
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value: Any):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value: Any):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def breadth_first_search(self, n: Any) -> bool:
        current = [self]
        next: list[BinaryTree] = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False

    def invert(self):
        current = [self]
        next: list[BinaryTree] = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            current = next
            next = []

    def has_leaf_nodes(self) -> bool:
        if self.left_child is None or self.right_child is None:
            return False
        if self.left_child.left_child is None or self.left_child.right_child is None:
            return False
        if self.left_child.right_child is None or self.right_child.right_child is None:
            return False
        return True


def invert(tree: BinaryTree):
    if tree:
        tmp = tree.left_child
        tree.left_child = tree.right_child
        tree.right_child = tmp
        invert(tree.left_child)
        invert(tree.right_child)


def preorder(tree: BinaryTree):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left_child.insert_left(4)
tree.right_child.insert_left(5)
tree.right_child.insert_right(6)
preorder(tree)
invert(tree)
preorder(tree)