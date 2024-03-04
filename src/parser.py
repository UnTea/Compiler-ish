import ast

from src.node.constant_node import create_constant_node
from src.node.nodes import NODES
from src.node.return_node import create_return_node
from src.node.start_node import create_start_node


def ast_to_node(tree):
    graph = {0: []}
    labels = {0: 'Start'}

    start = create_start_node()

    def walk_fields(node_id, tree):
        args = {}

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
                    args[field] = value

        return args

    def walk(parent_id, tree, field):
        node_id = len(graph)
        graph[parent_id].append(node_id)
        graph[node_id] = []

        match tree:
            case list():
                for idx, elem in enumerate(tree):
                    walk(node_id, elem, idx)

            case ast.FunctionDef():
                walk_fields(node_id, tree)

            case ast.Return():
                walk_fields(node_id, tree)

                node = create_return_node(
                    control=start,
                    data=NODES[start['_node_id'] + 1],
                )

                labels[node['_node_id']] = 'Return'

            case ast.BinOp():
                walk_fields(node_id, tree)

            case ast.Name() as child if child != []:
                walk_fields(node_id, tree)

            case ast.Mult() as child if child != []:
                pass

            case ast.Constant() as child if child != []:
                args = walk_fields(node_id, tree).get('value')

                node = create_constant_node(
                    value=args,
                    control=start,
                )

                labels[node['_node_id']] = f"Constant'\n'value:{args}"

            case ast.AST():
                walk_fields(node_id, tree)

    walk_fields(0, tree)

    return nodes_to_dot(NODES, labels)


# TODO: save for later
def get_error_details(source, node, filename=''):
    return (
        filename,
        node.linelo,
        node.col_offset + 1,
        ast.get_source_segment(source, node),
        node.end_linelo,
        node.end_col_offset + 1,
    )
