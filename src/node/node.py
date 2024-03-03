UNIQUE_ID = 1
NODES = []


def create_node(inputs=None):
    global UNIQUE_ID
    node_id = UNIQUE_ID
    UNIQUE_ID += 1

    inputs = inputs or []
    outputs = []

    for n in inputs:
        if n is not None:
            outputs.append(n)

    node = {
        "_node_id": node_id,
        "_inputs": inputs,
        "_outputs": outputs,
    }

    NODES.append(node)

    return node


def get_input(node, i):
    return node["_inputs"][i] if i < len(node["_inputs"]) else None


def get_num_inputs(node):
    return len(node["_inputs"])


def get_num_outputs(node):
    return len(node["_outputs"])


def is_unused(node):
    return get_num_outputs(node) == 0


def is_cfg(node):
    return False


def reset():
    global UNIQUE_ID
    UNIQUE_ID = 1
