"""
Module: data_structures.py
Description: This module contains implementations for basic data structures:
             - LinkedList
             - Stack
             - Queue
"""


class Node:
    """
    Represents a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A simple implementation of a singly linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        """
        Converts the linked list to a Python list.
        Returns:
        list: A list containing all the elements of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


class Stack:
    """
    A simple stack implementation using a Python list.
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Pushes an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pops an item from the stack.
        Returns:
        The popped item, or None if the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """
        Returns the top item of the stack without removing it.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns:
        bool: True if empty, False otherwise.
        """
        return len(self.items) == 0


class Queue:
    """
    A simple queue implementation using a Python list.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.
        Returns:
        The dequeued item, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        """
        Checks if the queue is empty.
        Returns:
        bool: True if empty, False otherwise.
        """
        return len(self.items) == 0


if __name__ == "__main__":

    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    print("LinkedList contents:", ll.to_list())

    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack top element:", stack.peek())
    print("Popped from stack:", stack.pop())

    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    print("Dequeued from queue:", queue.dequeue())
