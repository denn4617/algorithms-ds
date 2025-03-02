import unittest
from src.data_structures import LinkedList, Stack, Queue


class TestDataStructures(unittest.TestCase):
    def test_linked_list(self):
        # Create a linked list and verify its conversion to a list.
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_stack(self):
        # Test basic stack operations.
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(10)
        stack.push(20)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertIsNone(stack.pop())

    def test_queue(self):
        # Test basic queue operations.
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue("first")
        queue.enqueue("second")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.dequeue(), "second")
        self.assertIsNone(queue.dequeue())


if __name__ == "__main__":
    unittest.main()
