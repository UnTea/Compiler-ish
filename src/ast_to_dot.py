import ast
import os
from collections import defaultdict


class ASTVisualizer:
    def __init__(self):
        self.graph = defaultdict(list)
        self.labels = {}

    def ast_visitor(self, tree):
        stack = [(None, tree)]
        parent_id = None

        while stack:
            parent_id, current_node = stack.pop()

            if isinstance(current_node, ast.AST):
                node_id = len(self.graph)
                self.graph[node_id] = []
                self.labels[node_id] = type(current_node).__name__

                if parent_id is not None:
                    self.graph[parent_id].append(node_id)

                for field in reversed(current_node._fields):
                    stack.append((node_id, getattr(current_node, field)))

            elif isinstance(current_node, list):
                for element in reversed(current_node):
                    stack.append((parent_id, element))

        return parent_id

    def generate_dot_code(self):
        print("digraph AST {")
        self.print_nodes_dot(0)
        print("}")

    def print_nodes_dot(self, node_id, visited=None):
        if visited is None:
            visited = set()

        if node_id in visited:
            return

        visited.add(node_id)
        print(f'\t"{node_id}" [label = "{self.labels[node_id]}"]')

        for child_id in self.graph[node_id]:
            print(f'\t"{node_id}" -> "{child_id}"')
            self.print_nodes_dot(child_id, visited)

    def load_from_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")

            return

        with open(file_path, 'r') as f:
            source_code = f.read()

        tree = ast.parse(source_code)
        self.ast_visitor(tree)


if __name__ == "__main__":
    visualizer = ASTVisualizer()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_file_path = os.path.join(script_dir, "..", "tests", "test_file.py")

    visualizer.load_from_file(test_file_path)
    visualizer.generate_dot_code()
