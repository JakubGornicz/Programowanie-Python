from typing import Any


class BinaryNode(object):
    value: Any

    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.children = []

    def __repr__(self):
        return str(self.value)

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

    @property
    def get_level(self) -> int:
        level = 0
        temp = self.parent
        while temp is not None:
            level += 1
            temp = temp.parent

        return level

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

    def traverse_in_order(self, start, path=''):
        if start:
            path = self.traverse_in_order(start.left, path)
            path += str(start.value)
            path = self.traverse_in_order(start.right, path)
        return path

    def traverse_post_order(self, start, path=''):
        if start:
            path = self.traverse_in_order(start.left, path)
            path = self.traverse_in_order(start.right, path)
            path += str(start.value)
        return path

    def traverse_pre_order(self, start, path: str):
        if start:
            path += str(start.value)
            path = self.traverse_pre_order(start.left, path)
            path = self.traverse_pre_order(start.right, path)
        return path

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


class BinaryTree(object):
    root: BinaryNode

    def __init__(self, root):
        self.root = BinaryNode(root)

    def traverse_in_order(self, start, path=''):
        if start:
            path = self.traverse_in_order(start.left, path)
            path += str(start.value)
            path = self.traverse_in_order(start.right, path)
        return path

    def traverse_post_order(self, start, path=''):
        if start:
            path = self.traverse_in_order(start.left, path)
            path = self.traverse_in_order(start.right, path)
            path += str(start.value)
        return path

    def traverse_pre_order(self, start, path=''):
        if start:
            path += str(start.value)
            path = self.traverse_pre_order(start.left, path)
            path = self.traverse_pre_order(start.right, path)
        return path

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


tree = BinaryTree(1)
tree.root.add_left_child(2)
tree.root.add_right_child(3)
tree.root.left.add_left_child(4)
tree.root.left.add_right_child(5)
tree.root.right.add_left_child(6)
tree.root.right.add_right_child(7)
tree.root.left.right.add_left_child(13)
tree.root.left.right.add_right_child(12)
#                  1
#               /     \
#              2       3
#             / \     / \
#            4   5   6   7


print(tree.root)
print(tree.root.is_leaf())
print(tree.root.left.is_leaf())
print(tree.root.left.left.is_leaf())

print(tree.traverse_pre_order(tree.root))
print(tree.traverse_in_order(tree.root))
print(tree.traverse_post_order(tree.root))
tree.show()

print("\n")
node = BinaryNode('Parent')
node.add_left_child('Child1')
node.add_right_child('Child2')
node.left.add_left_child('Grandchild1')
node.show()
