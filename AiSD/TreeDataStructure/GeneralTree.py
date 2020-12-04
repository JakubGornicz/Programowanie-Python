from collections import deque
from typing import Any, List, Callable


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def is_leaf(self):
        if self.children:
            return False
        else:
            return True

    def add(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        temp = self.parent
        while temp is not None:
            level += 1
            temp = temp.parent

        return level

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)
            print(i)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        visit(self)
        queue = self.children
        for i in queue:
            visit(i)
            for j in i.children:
                queue.append(j)
            print(i)

    def print_tree(self):
        indentation = ' ' * self.get_level() * 3
        if self.parent:
            prefix = indentation + "|__"
        else:
            prefix = ""
        print(prefix + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()

    def __repr__(self):
        return self.value

    """
        def search(self, value: Any):
            def serch_tree(self):
                if(self.value == value):
                    return True
            return_value = self.for_each_deep_first(serch_tree)
            if(return_value == None):
                return False
            else:
                return True
    """


class Tree:
    root: TreeNode

    def __init__(self, node):
        self.root = node

    def add(self, value: Any, parent_value: Any):
        parent_value.children.append(TreeNode(value))
        parent_value.children[-1].value = value

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        self.root.for_each_level_order(visit)


root = TreeNode("Zwierze")

node1 = TreeNode("Ssak")
node1.add(TreeNode("Delfin"))
node1.add(TreeNode("Krowa"))
leaf_node1_3 = TreeNode("Tygrys")
node1.add(leaf_node1_3)

node2 = TreeNode("Gad")
node2.add(TreeNode("Aligator"))
node2.add(TreeNode("Wąż"))
node2.add(TreeNode("Żółw"))

node3 = TreeNode("Ptak")
node3.add(TreeNode("Papuga"))
node3.add(TreeNode("Sowa"))

root.add(node1)
root.add(node2)
root.add(node3)

root.print_tree()

print("\n# test metody is_leaf")
print(f"Dla węzła {root.value} metoda zwraca: {root.is_leaf()}")
print(f"Dla węzła {node1.value} metoda zwraca: {node1.is_leaf()}")
print(f"Dla węzła {leaf_node1_3.value} metoda zwraca: {leaf_node1_3.is_leaf()}")





