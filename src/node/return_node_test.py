import unittest

from node import (
    get_num_inputs,
    get_num_outputs,
    create_node,
)
from return_node import (
    create_return_node,
    get_ctrl,
    get_expr,
)


class TestReturnNode(unittest.TestCase):
    def test_create_return_node(self):
        ctrl_node = create_node()
        data_node = create_node()
        return_node = create_return_node(ctrl_node, data_node)

        self.assertIsNotNone(return_node)
        self.assertEqual(get_num_inputs(return_node), 2)
        self.assertEqual(get_num_outputs(return_node), 2)
        self.assertEqual(get_ctrl(return_node), ctrl_node)
        self.assertEqual(get_expr(return_node), data_node)


if __name__ == '__main__':
    unittest.main()
