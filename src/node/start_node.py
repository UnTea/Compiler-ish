from src.node.nodes import create_node


def create_start_node(inputs=None):
    if inputs is None:
        inputs = []

    start_node = create_node(inputs=inputs, is_start=True)

    return start_node


def is_cfg():
    return True
