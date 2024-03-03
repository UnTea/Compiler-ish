from node import create_node, NODES


def create_constant_node(value):
    constant_node = create_node([None])
    constant_node["_value"] = value
    NODES.append(constant_node)

    return constant_node


def get_constant_value(constant_node):
    return constant_node.get('_value', None)
