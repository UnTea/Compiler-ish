import unittest

from node import (
    create_node,
    get_num_inputs,
    get_num_outputs,
    is_unused,
    reset,
)


class TestBaseNodes(unittest.TestCase):
    def setUp(self):
        reset()

    def test_create_node(self):
        node = create_node()
        self.assertIsNotNone(node)
        self.assertEqual(get_num_inputs(node), 0)
        self.assertEqual(get_num_outputs(node), 0)

    def test_create_node_with_inputs(self):
        input_node1 = create_node()
        input_node2 = create_node()
        node = create_node([input_node1, input_node2])
        self.assertIsNotNone(node)
        self.assertEqual(get_num_inputs(node), 2)
        self.assertEqual(get_num_outputs(node), 2)

    def test_create_unused_node(self):
        node = create_node()
        self.assertTrue(is_unused(node))


if __name__ == '__main__':
    unittest.main()
