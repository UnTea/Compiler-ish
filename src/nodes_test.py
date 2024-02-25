import unittest
from nodes import (
    create_start_block,
    create_stop_block,
    create_constant_block,
    connect_blocks,
    create_basic_block,
    graph,
)
from src.dot import node_to_dot


class TestSeaOfNodes(unittest.TestCase):
    def test_graph_creation(self):
        start_block = create_start_block()
        return_block = create_basic_block()
        constant_block = create_constant_block(1)
        stop_block = create_stop_block()

        connect_blocks(start_block, return_block)
        connect_blocks(return_block, constant_block)
        connect_blocks(return_block, stop_block)
        connect_blocks(constant_block, stop_block)

        print(node_to_dot(graph))


if __name__ == '__main__':
    unittest.main()
