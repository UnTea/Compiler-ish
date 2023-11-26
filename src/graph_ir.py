import ast


def build_graph_ir(tree, graph_ir):
    stack = [(None, tree)]
    parent_id = None
    object_counter = 0

    while stack:
        parent_id, current_node = stack.pop()

        if isinstance(current_node, ast.AST):
            object_id = id(current_node)
            node_id = len(graph_ir)
            graph_ir[node_id] = {'label': type(current_node).__name__, 'object_id': object_id, 'children': []}

            if parent_id is not None:
                graph_ir[parent_id]['children'].append(object_id)

            for field in reversed(current_node._fields):
                stack.append((node_id, getattr(current_node, field)))

        elif isinstance(current_node, list):
            for element in reversed(current_node):
                stack.append((parent_id, element))


def build_graph(tree, graph, labels):
    stack = [(None, tree)]
    parent_id = None

    while stack:
        parent_id, current_node = stack.pop()

        if isinstance(current_node, ast.AST):
            node_id = len(graph)
            graph[node_id] = {'type': type(current_node).__name__, 'children': []}
            labels[node_id] = type(current_node).__name__

            if parent_id is not None:
                graph[parent_id]['children'].append(node_id)

            for field in reversed(current_node._fields):
                stack.append((node_id, getattr(current_node, field)))

        elif isinstance(current_node, list):
            for element in reversed(current_node):
                stack.append((parent_id, element))

    return parent_id


def generate_dot_code(graph, labels):
    print("digraph AST {")
    print_nodes_dot(0, graph, labels)
    print("}")


def print_nodes_dot(node_id, graph, labels, visited=None):
    if visited is None:
        visited = set()

    if node_id in visited:
        return

    visited.add(node_id)
    print(f'\t"{node_id}" [label = "{labels[node_id]}"]')

    for child_id in graph[node_id]['children']:
        print(f'\t"{node_id}" -> "{child_id}"')
        print_nodes_dot(child_id, graph, labels, visited)
