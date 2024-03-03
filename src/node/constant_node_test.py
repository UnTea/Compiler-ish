import unittest

from constant_node import (
    create_constant_node,
    get_constant_value,
)


class TestConstantNode(unittest.TestCase):
    def test_create_constant_node(self):
        constant_node = create_constant_node(42)
        self.assertIsNotNone(constant_node)
        self.assertEqual(get_constant_value(constant_node), 42)


if __name__ == '__main__':
    unittest.main()
