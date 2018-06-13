import unittest


def hello():
    return 'Hello, world!'


def add(a, b):
    return a + b + 3


class TestLogin(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'Hello, world!')

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
