class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self):
        self.head = None

    def __len__(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def __repr__(self):
        temp = self.head
        nodes = []
        while temp is not None:
            nodes.append(str(temp.value))
            temp = temp.next
        return "\n".join(nodes)

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is already empty")
            return None
        else:
            removed_val = self.head.value
            self.head = self.head.next
            return removed_val


if __name__ == "__main__":
    stack = Stack()
    assert len(stack) == 0  # test 1
    stack.push(3)
    stack.push(10)
    stack.push(1)

    assert len(stack) == 3  # test 2
    print(stack)

    print("\n")

    top_value = stack.pop()
    assert top_value == 1  # test 3
    print(stack)

    assert len(stack) == 2  # test 4
