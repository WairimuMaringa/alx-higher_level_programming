#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @property
    def next_node(self):
        return (self.__next_node)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __str__(self):
        rtrn = ""
        ptr = self.__head

        while ptr is not None:
            rtrn += str(ptr.data)
            if ptr.next_node is not None:
                rtrn += "\n"
            ptr = ptr.next_node

        return (rtrn)

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        new_node = Node(value, ptr)
        if ptr == self.__head:
            self.__head = new_node
        else:
            ptr_prev.next_node = new_node
