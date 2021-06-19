import sys
sys.path.append("models/lists")
from aed_ds.lists.adt_list import List
from aed_ds.lists.nodes import SingleListNode
from aed_ds.singly_linked_list_iterator import SinglyLinkedListIterator
from aed_ds.exceptions import EmptyListException
from aed_ds.exceptions import InvalidPositionException

class SinglyLinkedList(List):
    def __init__(self):
        self.tail = SingleListNode(None, None)
        self.head = SingleListNode(None, self.tail)

    def is_empty(self) -> bool:
        if self.head.element == None:
            return True
        return False

    def size(self) -> int:
        if self.is_empty() == True:
            return 0
        node = self.head
        count = 0
        while node != self.tail:
            if node.element != None:
                count += 1
            node = node.next_node
        return int(count)

    def get(self, position: int) -> object:
        node = self.head
        count = 0
        while count < self.size() or count != position:
            node = node.get_next_node()
            count += 1
        return node.get_element()

    def get_first(self) -> object:
        if not self.is_empty():
            return self.head.element
        raise EmptyListException("The lists is empty. Cannot return first!")

    def get_last(self) -> object:
        if not self.is_empty():
            return self.tail.element
        raise EmptyListException("The lists is empty. Cannot return first!")

    def find(self, element: object) -> bool:
        if self.is_empty() == False:
            node = self.head
            p = 0
            while p < self.size():
                if element == node.get_element():
                    return p
                node = node.get_next_node()
                p += 1
        return -1

    def insert_first(self, element: object) -> None:
        if self.head.element == None:
            self.head = SingleListNode(element, self.head.get_next_node())
        elif self.head.element != None and self.tail.element == None:
            self.tail.set_element(self.head.element)
            self.head.set_element(element)
        else:
            node = SingleListNode(element, self.head)
            self.head = node

    def insert_last(self, element: object) -> None:
        if self.head.get_element() == None:
            self.insert_first(element)
        elif self.tail.get_element() == None:
            self.tail.set_element(element)
        else:
            previous = self.head
            while previous.next_node != self.tail:
                previous = previous.next_node
            node = SingleListNode(element, None)
            previous.set_next_node(self.tail)
            self.tail.set_next_node(node)
            self.tail = node

    def insert(self, element: object, position: int) -> None:
        if position == self.size():
            self.insert_last(element)
        elif position == 0:
            self.insert_first(element)
        else:
            if position >= 0 and position <= self.size():
                count = 0
                node = self.head
                while count != position - 1:
                    node = node.get_next_node()
                    count += 1
                newNode = SingleListNode(element, node.get_next_node().get_next_node())
                node.set_next_node(newNode)
            else:
                raise InvalidPositionException("The given position is not a valid position")

    def remove_first(self) -> object:
        if not self.is_empty():
            if self.head.get_next_node() == self.tail:
                self.head.set_element(self.tail.get_element())
                self.tail.set_element(None)
            else:
                node = self.head
                while node.get_next_node() != self.tail:
                    node.set_element(node.get_next_node().get_element())
                    node = node.get_next_node()
                self.tail = node
        else:
            raise EmptyListException("The lists is empty. Cannot remove first!")

    def remove_last(self) -> object:
        if not self.is_empty():
            node = self.head
            c = 0
            while c < self.size() - 1:
                node = node.get_next_node()
                c += 1
            nodeSol = self.tail
            self.tail = node
            self.tail.set_next_node(None)
            return nodeSol
        else:
            raise EmptyListException("The lists is empty. Cannot remove last!")

    def remove(self, position: int) -> object:
        if position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        if position >= 0 and position < self.size():
            i = 0
            node = self.head
            while i < position - 1:
                i += 1
                node = node.get_next_node()
            nodeSol = node.get_next_node()
            node.set_next_node(nodeSol.get_next_node())
            return nodeSol
        else:
            raise InvalidPositionException("The given position is not a valid position")

    def make_empty(self) -> None:
        i = self.size()
        n = 0
        node = self.head
        while n < i:
            n += 1
            node = node.get_next_node()
            self.head = None
            self.head = node
        self.head = None
        self.tail = None

    def iterator(self):
        iterator = SinglyLinkedListIterator(self.head)
        return iterator

    def __str__(self):
        node = self.head
        o = "["
        while node != self.tail:
            o += f"{node.__str__()}, "
            node = node.get_next_node()
        o += f"{node.__str__()}]"
        return o

    def __iter__(self):
        node = self.head
        if not self.is_empty():
            while node != None:
                if node.element == None:
                    break
                yield node.get_element()
                node = node.get_next_node()

    def __add__(self, other):
        if type(other).__name__ != type(self).__name__:
            raise Exception("Unable to add.")
        if not other.is_empty():
            for c in other:
                self.insert_last(c)
        return self

    def __eq__(self, other):
        if type(other).__name__ != type(self).__name__:
            raise Exception("Unable to compare.")
        if other.size() != self.size():
            return False
        for index, c in enumerate(other):
            if other[index] != c:
                return False
        return True

    def __getitem__(self, item):
        for index, c in enumerate(self):
            if index == item:
                return c
        raise Exception(f"{item} is not in the list.")

    def append(self, item):
        self.insert_last(item)


