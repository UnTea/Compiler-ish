import ast
import os
from graph_ir import build_graph, generate_dot_code, print_nodes_dot


def load_from_file(file_path, graph, labels):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r') as f:
        source_code = f.read()

    tree = ast.parse(source_code)
    build_graph(tree, graph, labels)


if __name__ == "__main__":
    graph = {}
    labels = {}

    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_file_path = os.path.join(script_dir, "..", "tests", "test_file.py")

    load_from_file(test_file_path, graph, labels)
    generate_dot_code(graph, labels)
