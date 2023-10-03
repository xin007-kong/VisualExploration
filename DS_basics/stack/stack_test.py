import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.items, [1, 2, 3])

    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_peek(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3)

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.size(), 3)

if __name__ == '__main__':
    unittest.main()