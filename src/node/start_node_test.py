import unittest

from src.node.node import (
    get_num_inputs,
    get_num_outputs,
)
from start_node import create_start_node


class TestStartNode(unittest.TestCase):
    def test_create_start_node(self):
        start_node = create_start_node()
        self.assertIsNotNone(start_node)
        self.assertEqual(get_num_inputs(start_node), 0)
        self.assertEqual(get_num_outputs(start_node), 0)


if __name__ == '__main__':
    unittest.main()
