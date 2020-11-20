class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        return " -> ".join(nodes)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def __len__(self):
        temp = self.head
        count = 0
        while temp.next is not None:
            count += 1
            temp = temp.next
        return count

    def node(self, at):
        if at >= self.__len__():
            print("Error: index out of range")
            return None
        temp_at = 0
        temp_node = self.head
        while True:
            temp_node = temp_node.next
            if temp_at == at:
                return temp_node
            temp_at += 1

    def insert(self, value, after):
        if not self.head:
            raise Exception("List is empty")
        new_node = Node(value)
        temp = self.head
        while temp.next != after:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def pop(self):
        if not self.head:
            raise Exception("List is empty")
        first_node = self.head
        self.head = first_node.next
        return first_node.value

    def remove_last(self, last_node):
        if not self.head:
            raise Exception("List is empty")
        temp = self.head
        while temp.next != last_node:
            temp = temp.next
        removed_node = temp.next
        temp.next = None
        return removed_node.value

    def remove(self, after):
        if not self.head:
            raise Exception("List is empty")
        temp = self.head
        while temp.next != after:
            temp = temp.next
        temp.next = after.next


list_ = LinkedList()
list_.push(1)
list_.push(0)
print(len(list_))

"""
list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1' # test 2 : wprowadziłem modyfikację aby łatwiej mi było nawigować się po liście
print(list_)

list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10' # test 3 : -||-
print(list_)

# print(list_.node(0)) # test czy node() zwraca węzeł 


middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10' # test 4 
print(list_)

first_element = list_.head
returned_first_element = list_.pop()
assert first_element.value == returned_first_element # test 5 
print(list_)

last_element = list_.node(at=2)
returned_last_element = list_.remove_last(last_element)

assert last_element.value == returned_last_element  # test 6  
assert str(list_) == '1 -> 5 -> 9'
print(list_)


second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5' # test 7
print(list_)
"""