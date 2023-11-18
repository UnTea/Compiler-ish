import ast
import sys


def ast_to_dot(node, parent_id=-1):
    if isinstance(node, ast.AST):
        node_id = hash(node)
        print(f'{node_id} [label="{type(node).__name__}"]')

        if parent_id != -1:
            print(f'{parent_id} -> {node_id}')

        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        ast_to_dot(item, node_id)

            elif isinstance(value, ast.AST):
                ast_to_dot(value, node_id)


def generate_dot_code(source_code):
    tree = ast.parse(source_code)
    print("digraph AST {")
    ast_to_dot(tree)
    print("}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ast_to_dot.py <source_file.py>")
        sys.exit(1)

    source_file = sys.argv[1]
    with open(source_file, 'r') as f:
        source_code = f.read()

    generate_dot_code(source_code)
