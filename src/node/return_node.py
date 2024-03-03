from node import create_node, get_input


def create_return_node(ctrl, data):
    return create_node([ctrl, data])


def get_ctrl(node):
    return get_input(node, 0)


def get_expr(node):
    return get_input(node, 1)


def is_cfg(node):
    return False
