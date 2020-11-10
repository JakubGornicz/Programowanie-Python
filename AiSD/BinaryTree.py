from typing import Any


class BinaryNode:
    value: Any

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.children = []
        self.parent = None

    def __repr__(self):
        return str(self.value)

    def add_right_child(self, new_child):
        new_child.parent = self
        self.right_child = new_child
        self.children.append(new_child)

    def add_left_child(self, new_child):
        new_child.parent = self
        self.left_child = new_child
        self.children.append(new_child)

    @property
    def get_level(self):
        level = 0
        temp = self.parent
        while temp is not None:
            level += 1
            temp = temp.parent

        return level

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def print_tree(self):
        indentation = ' ' * self.get_level * 3
        if self.parent:
            prefix = indentation + "|__"
        else:
            prefix = ""
        print(prefix + str(self.value))
        if self.children:
            for child in self.children:
                if child:
                    child.print_tree()


"""
class BinaryTree(BinaryNode):
    root: BinaryNode
    def __init__(self, value):
        self.root = value

    def print_tree(self):
        indentation = ' ' * self.get_level() * 3
        if self.parent:
            prefix = indentation + "|__"
        else:
            prefix = ""
        print(prefix + str(self.value))
        if self.children:
            for child in self.children:
                if child:
                    child.print_tree()        
"""
root = BinaryNode("human")
print("printing object of type 'BinaryNode':", root, '\n')

female = BinaryNode("female")

woman = BinaryNode("woman")
girl = BinaryNode("girl")
female.add_right_child(woman)
female.add_left_child(girl)

male = BinaryNode("male")

man = BinaryNode("man")
boy = BinaryNode("boy")
male.add_right_child(man)
male.add_left_child(boy)

strong = BinaryNode("strong")
man.add_right_child(strong)

root.add_right_child(female)
root.add_left_child(male)

print("graphic representation of the binary tree: ")
root.print_tree()
print('\nis human a leaf?:', root.is_leaf())
print('is girl a leaf?:', girl.is_leaf())
print('is strong a leaf?:', strong.is_leaf())
