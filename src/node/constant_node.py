from src.node.nodes import create_node


def create_constant_node(value, control=None):
    if control is None:
        control = []

    constant_node = create_node(inputs=control)
    constant_node["_value"] = value

    return constant_node


def is_cfg():
    return False
