UNIQUE_ID = 1
NODES = []


def get_unique_id():
    global UNIQUE_ID
    _id = UNIQUE_ID
    UNIQUE_ID += 1

    return _id


def create_node(inputs=None, is_start=False):
    _node_id = 0 if is_start else get_unique_id()
    _inputs = []
    _outputs = inputs if inputs is None or isinstance(inputs, list) else [inputs]

    node = {
        '_node_id': _node_id,
        '_inputs': _inputs,
        '_outputs': _outputs,
    }

    for n in _outputs:
        if n is not None:
            n['_inputs'].append(node)

    NODES.append(node)

    return node


def get_input(node, i):
    return node['_inputs'][i] if i < len(node['_inputs']) else None


def get_num_inputs(node):
    return len(node['_inputs'])


def get_num_outputs(node):
    return len(node['_outputs'])


def is_unused(node):
    return get_num_outputs(node) == 0


def is_cfg():
    return False


def reset():
    global UNIQUE_ID
    UNIQUE_ID = 1
