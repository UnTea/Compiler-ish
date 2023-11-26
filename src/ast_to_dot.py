import ast
import os
from graph_ir import build_graph_ir


def load_from_file(file_path, graph_ir):
    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return

    with open(file_path, 'r') as f:
        source_code = f.read()

    tree = ast.parse(source_code)
    build_graph_ir(tree, graph_ir)


def generate_dot_code(graph_ir):
    print("digraph AST {")
    print_nodes_dot(graph_ir)
    print("}")


def print_nodes_dot(graph_ir):
    for node_id, data in graph_ir.items():
        label = data['label']
        object_id = data.get('object_id', 'None')
        print(f'\t"{object_id}" [label = "{label}"]')

        children = data.get('children', [])
        for child_id in children:
            print(f'\t"{object_id}" -> "{child_id}"')


if __name__ == "__main__":
    graph_ir = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_file_path = os.path.join(script_dir, "..", "tests", "test_file.py")

    load_from_file(test_file_path, graph_ir)
    generate_dot_code(graph_ir)
