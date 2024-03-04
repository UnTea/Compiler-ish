from src.node.nodes import create_node


def create_return_node(control=None, data=None):
    if control is None:
        control = []

    if data is None:
        data = None

    return create_node(inputs=[control, data])


def get_control(node):
    return node['_inputs'][0]


def get_expression(node):
    return node['_inputs'][1]


def is_cfg():
    return True
