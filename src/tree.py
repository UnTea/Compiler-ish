import ast

from ast import dump


def get_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        return content
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None

    except Exception as error:
        print(f"An error occurred while reading {file_path} file : {error}")
        return None


def get_ast_tree(file_content):
    try:
        return ast.parse(file_content)

    except SyntaxError as error:
        print(f"Syntax error when parsing AST: {error}")
        return None

    except Exception as error:
        print(f"An error occurred while parsing AST: {error}")
        return None


def ast_dump(tree, indent=4, annotate_fields=False, include_attributes=False):
    return dump(
        tree,
        indent=indent,
        annotate_fields=annotate_fields,
        include_attributes=include_attributes,
    )
