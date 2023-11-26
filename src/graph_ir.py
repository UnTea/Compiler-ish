import ast
from typing import Optional


def analyze_expression_dependencies(graph, expr_node_id):
    """
    Анализирует зависимости в выражении и возвращает список списков,
    где каждый список представляет собой группу узлов, которые можно близко расположить.
    """
    dependencies = []

    def traverse_dependencies(node_id, current_dependency):
        if node_id not in graph:
            return

        current_dependency.append(node_id)
        children = graph[node_id].get('children', [])

        for child_id in children:
            traverse_dependencies(child_id, current_dependency)

    traverse_dependencies(expr_node_id, [])

    return dependencies


def optimize_graph_positions(graph, labels):
    for node_id, data in graph.items():
        if 'label' in data and data['label'] == 'foo':
            if 'children' in data:
                for child_id in data['children']:
                    child_data = graph[child_id]
                    if 'label' in child_data and child_data['label'] == 'Expr':
                        dependencies = analyze_expression_dependencies(graph, child_id)

                        # Базовая оптимизация: вычисление центра масс по горизонтали
                        total_x = 0
                        total_nodes = 0

                        for group in dependencies:
                            for node in group:
                                total_x += node % 10  # Просто для примера, можно использовать реальные координаты
                                total_nodes += 1

                        if total_nodes > 0:
                            center_of_mass = total_x / total_nodes

                            # Перемещение узлов к центру масс
                            for group in dependencies:
                                for node in group:
                                    # Просто для примера, здесь нужно обновить координаты узла в графе
                                    graph[node]['x'] = center_of_mass
                                    graph[node]['y'] = 0

                            print("Optimizing positions for expression:", child_data['label'])
                            print("New positions:", graph)


def get_node_info(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Name):
        return f"Name: {node.id}"
    elif isinstance(node, ast.FunctionDef):
        return f"Function: {node.name}"
    elif isinstance(node, ast.Constant):
        return f"Constant: {repr(node.value)}"
    return None


def build_graph_ir(tree, graph_ir):
    stack = [(None, tree)]
    parent_id = None
    object_counter = 0

    while stack:
        parent_id, current_node = stack.pop()

        if isinstance(current_node, ast.AST):
            object_id = id(current_node)
            node_id = len(graph_ir)
            label = type(current_node).__name__
            additional_info = get_node_info(current_node)
            if additional_info:
                label += f"\n{additional_info}"

            graph_ir[node_id] = {'label': label, 'object_id': object_id, 'children': []}

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
