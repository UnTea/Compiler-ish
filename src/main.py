import os

from dot import ast_to_dot
from tree import get_file_content, get_ast_tree


def main():
    fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_file.py")
    fc = get_file_content(fp)
    ast_tree = get_ast_tree(fc)
    print(ast_to_dot(ast_tree))


if __name__ == '__main__':
    main()
