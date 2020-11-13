from typing import Any


class BinaryNode(object):
    value: Any

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.children = []

    def min(self):
        if self.left:
            temp = self.left
            while temp.value > temp.left.value:
                temp = temp.left
            return temp
        else:
            return self

    def __repr__(self):
        return str(self.value)

    def add_left_child(self, value: Any):
        new_node = BinaryNode(value)
        new_node.parent = self
        self.left = new_node
        self.children.append(new_node)

    def add_right_child(self, value: Any):
        new_node = BinaryNode(value)
        new_node.parent = self
        self.right = new_node
        self.children.append(new_node)

    @property
    def get_level(self) -> int:
        level = 0
        temp = self.parent
        while temp is not None:
            level += 1
            temp = temp.parent

        return level

    def show(self):
        indentation = ' ' * self.get_level * 4
        if self.parent:
            prefix = indentation + "|___"
        else:
            prefix = "    "
        print(prefix + str(self.value))
        if self.children:
            for child in self.children:
                if child:
                    child.show()


class BinarySearchTree(object):
    root: BinaryNode

    def __init__(self, root):
        self. root = BinaryNode(root)

    @property
    def get_level(self) -> int:
        level = 0
        temp = self.root.parent
        while temp is not None:
            level += 1
            temp = temp.parent

        return level

    def show(self):
        indentation = ' ' * self.get_level * 4
        if self.root.parent:
            prefix = indentation + "|___"
        else:
            prefix = "    "
        print(prefix + str(self.root.value))
        if self.root.children:
            for child in self.root.children:
                if child:
                    child.show()


node = BinaryNode(10)
node.add_left_child(6)
node.add_right_child(11)
node.left.add_left_child(3)





node.show()
