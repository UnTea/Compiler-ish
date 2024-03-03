import unittest

from constant_node import create_constant_node, get_constant_value
from node import (
    get_num_inputs,
    get_num_outputs,
    is_unused,
    reset,
)
from return_node import create_return_node, get_ctrl, get_expr
from start_node import create_start_node, is_start_cfg


def create_sample_program():
    start_node = create_start_node()
    constant_node = create_constant_node(1)
    return_node = create_return_node(start_node, constant_node)

    return start_node, constant_node, return_node


class TestSampleProgram(unittest.TestCase):
    def setUp(self):
        reset()

    def test_sample_program(self):
        start_node, constant_node, return_node = create_sample_program()

        self.assertIsNotNone(start_node)
        self.assertEqual(get_num_inputs(start_node), 0)
        self.assertEqual(get_num_outputs(start_node), 0)
        self.assertTrue(is_unused(start_node))
        self.assertFalse(is_start_cfg(start_node))

        self.assertIsNotNone(constant_node)
        self.assertEqual(get_constant_value(constant_node), 1)

        self.assertIsNotNone(return_node)
        self.assertEqual(get_ctrl(return_node), start_node)
        self.assertEqual(get_expr(return_node), constant_node)


if __name__ == '__main__':
    unittest.main()
