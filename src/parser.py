import ast

from src.dot import to_dot


def ast_to_node(tree):
    graph = {0: []}
    labels = {0: type(tree).__name__}
    edge_labels = {}

    def walk_fields(node_id, tree):
        args = []

        for field in tree._fields:
            match getattr(tree, field):
                case list() as child if child != []:
                    walk(node_id, child, field)

                case ast.BinOp() as child if child != []:
                    walk(node_id, child, field)

                case ast.Name() as child if child != []:
                    walk(node_id, child, field)

                case ast.Mult() as child if child != []:
                    walk(node_id, child, field)

                case ast.Constant() as child if child != []:
                    walk(node_id, child, field)

                case ast.AST() as child if child != []:
                    walk(node_id, child, field)

                case _ as value:
                    args.append(f'{field}: {repr(value)}')

        return '\\n'.join(arg for arg in args)

    def walk(parent_id, tree, field):
        node_id = len(graph)
        graph[parent_id].append(node_id)
        graph[node_id] = []
        edge_labels[(parent_id, node_id)] = field

        match tree:
            case list():
                labels[node_id] = 'list'

                for idx, elem in enumerate(tree):
                    walk(node_id, elem, idx)

            case ast.FunctionDef():
                walk_fields(node_id, tree)
                labels[node_id] = f'{type(tree).__name__}'

            case ast.Return():
                walk_fields(node_id, tree)
                labels[node_id] = f'{type(tree).__name__}'

            case ast.BinOp():
                walk_fields(node_id, tree)
                labels[node_id] = f'{type(tree).__name__}'

            case ast.Name() as child if child != []:
                args = walk_fields(node_id, tree)
                labels[node_id] = f'{type(tree).__name__}\\n{args}'

            case ast.Mult() as child if child != []:
                labels[node_id] = f'{type(tree).__name__}'

            case ast.Constant() as child if child != []:
                args = walk_fields(node_id, tree)
                labels[node_id] = f'{type(tree).__name__}\\n{args}'

            case ast.AST():
                args = walk_fields(node_id, tree)
                labels[node_id] = f'{type(tree).__name__}\\n{args}'

    walk_fields(0, tree)

    return to_dot(graph, labels, edge_labels)


def get_error_details(source, node, filename=''):
    return (
        filename,
        node.linelo,
        node.col_offset + 1,
        ast.get_source_segment(source, node),
        node.end_linelo,
        node.end_col_offset + 1,
    )
