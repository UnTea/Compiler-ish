import ast
from _ast import Module


def get_file_content(file_path: str) -> str | None:
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


def get_ast_tree(file_content) -> Module | None:
    try:
        return ast.parse(file_content)

    except SyntaxError as error:
        print(f"Syntax error when parsing AST: {error}")
        return None

    except Exception as error:
        print(f"An error occurred while parsing AST: {error}")
        return None
